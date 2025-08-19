# example_queries.py
import sqlite3

DB = "yb_college.db"

def print_rows(title, rows, cols):
    print(f"\n=== {title} ===")
    print(" | ".join(cols))
    for r in rows:
        print(" | ".join(str(x) if x is not None else "" for x in r))

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        # 1) List Students with their Classes & Course names
        q1 = """
        SELECT s.Name AS Student, co.CourseName, cl.Schedule
        FROM Enrollment e
        JOIN Student s ON s.StudentID = e.StudentID
        JOIN Class   cl ON cl.ClassID   = e.ClassID
        JOIN Course  co ON co.CourseID  = cl.CourseID
        ORDER BY s.Name;
        """
        cur = conn.execute(q1)
        rows = cur.fetchall()
        print_rows("Students & Their Enrolled Classes", rows, ["Student", "CourseName", "Schedule"])

        # 2) Classes and who teaches them
        q2 = """
        SELECT co.CourseName, l.Name AS Lecturer, cl.Schedule
        FROM Class cl
        JOIN Course co  ON co.CourseID   = cl.CourseID
        JOIN Lecturer l ON l.LecturerID  = cl.LecturerID
        ORDER BY co.CourseName;
        """
        cur = conn.execute(q2)
        rows = cur.fetchall()
        print_rows("Classes & Lecturers", rows, ["CourseName", "Lecturer", "Schedule"])

        # 3) Enrollment count by Course
        q3 = """
        SELECT co.CourseName, COUNT(e.EnrollmentID) AS Enrolled
        FROM Course co
        JOIN Class  cl ON cl.CourseID = co.CourseID
        LEFT JOIN Enrollment e ON e.ClassID = cl.ClassID
        GROUP BY co.CourseID
        ORDER BY Enrolled DESC, co.CourseName;
        """
        cur = conn.execute(q3)
        rows = cur.fetchall()
        print_rows("Enrollment Count by Course", rows, ["CourseName", "Enrolled"])

if __name__ == "__main__":
    main()
