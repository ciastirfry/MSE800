# seed_data.py
import sqlite3

DB = "yb_college.db"

STUDENTS = [
    ("Magic Johnson", 54, "44 Magic St", "magic@mmba.com"),
    ("Charles Parker", 28, "56 Albert Ave", "charles@pba.com"),
    ("Bruce Lee", 33, "36 China Rd", "bruce@ddmb.com"),
]

LECTURERS = [
    ("Dr. Allan", "Computer Enigneering", "allan@yb.ac.nz"),
    ("Dr. Pablo", "Programming", "pablo@yb.ac.nz"),
]

COURSES = [
    ("Programming", 23, "Computer Enigneering"),
    ("Computer Engineering", 20, "Computer Enigneering"),
]

CLASSES = [
    # (CourseName, LecturerName, Schedule)
    ("Programming", "Dr. Allan", "Wed 11:00-12:00 Room C4"),
    ("Computer Engineering", "Dr. Pablo", "Tue 15:00-16:00 Room A5"),
]

ENROLLMENTS = [
    # (StudentEmail, CourseName) -> we’ll map to ClassID for the first class of that course
    ("magic@mmba.com", "Programming"),
    ("charles@pba.com", "Programming"),
    ("bruce@ddmb.com", "Computer Engineering"),
]

def get_id_by(conn, table, key_col, key_val, id_col):
    cur = conn.execute(f"SELECT {id_col} FROM {table} WHERE {key_col} = ?", (key_val,))
    row = cur.fetchone()
    return row[0] if row else None

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        # Insert Students
        conn.executemany(
            "INSERT OR IGNORE INTO Student (Name, Age, Address, Email) VALUES (?, ?, ?, ?)",
            STUDENTS
        )

        # Insert Lecturers
        conn.executemany(
            "INSERT OR IGNORE INTO Lecturer (Name, Department, Email) VALUES (?, ?, ?)",
            LECTURERS
        )

        # Insert Courses
        conn.executemany(
            "INSERT OR IGNORE INTO Course (CourseName, Credits, Department) VALUES (?, ?, ?)",
            COURSES
        )

        # Insert Classes (map CourseName, LecturerName to IDs)
        for course_name, lecturer_name, sched in CLASSES:
            course_id = get_id_by(conn, "Course", "CourseName", course_name, "CourseID")
            lecturer_id = get_id_by(conn, "Lecturer", "Name", lecturer_name, "LecturerID")
            conn.execute(
                "INSERT INTO Class (CourseID, LecturerID, Schedule) VALUES (?, ?, ?)",
                (course_id, lecturer_id, sched)
            )

        # Insert Enrollments (map StudentEmail and CourseName -> first matching Class)
        for email, course_name in ENROLLMENTS:
            student_id = get_id_by(conn, "Student", "Email", email, "StudentID")
            # pick first class for the course
            cur = conn.execute("""
                SELECT c.ClassID
                FROM Class c
                JOIN Course co ON c.CourseID = co.CourseID
                WHERE co.CourseName = ?
                ORDER BY c.ClassID ASC
                LIMIT 1
            """, (course_name,))
            class_row = cur.fetchone()
            if class_row and student_id:
                conn.execute(
                    "INSERT OR IGNORE INTO Enrollment (StudentID, ClassID) VALUES (?, ?)",
                    (student_id, class_row[0])
                )

        conn.commit()
    print("Seed data inserted.")

if __name__ == "__main__":
    main()
