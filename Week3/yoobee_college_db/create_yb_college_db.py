# create_schema.py
import sqlite3

DB = "yb_college.db"

DDL = """
PRAGMA foreign_keys = ON;

-- 1) Student
CREATE TABLE IF NOT EXISTS Student (
    StudentID     INTEGER PRIMARY KEY AUTOINCREMENT,
    Name          TEXT NOT NULL,
    Age           INTEGER CHECK (Age >= 0),
    Address       TEXT,
    Email         TEXT UNIQUE
);

-- 2) Lecturer
CREATE TABLE IF NOT EXISTS Lecturer (
    LecturerID    INTEGER PRIMARY KEY AUTOINCREMENT,
    Name          TEXT NOT NULL,
    Department    TEXT,
    Email         TEXT UNIQUE
);

-- 3) Course
CREATE TABLE IF NOT EXISTS Course (
    CourseID      INTEGER PRIMARY KEY AUTOINCREMENT,
    CourseName    TEXT NOT NULL,
    Credits       INTEGER NOT NULL CHECK (Credits BETWEEN 0 AND 60),
    Department    TEXT
);

-- 4) Class (a specific offering of a Course, taught by a Lecturer)
CREATE TABLE IF NOT EXISTS Class (
    ClassID       INTEGER PRIMARY KEY AUTOINCREMENT,
    CourseID      INTEGER NOT NULL,
    LecturerID    INTEGER NOT NULL,
    Schedule      TEXT, -- e.g., "Mon 10:00-12:00 Room A1"
    FOREIGN KEY (CourseID)  REFERENCES Course(CourseID)   ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (LecturerID)REFERENCES Lecturer(LecturerID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 5) Enrollment (student takes a class)
CREATE TABLE IF NOT EXISTS Enrollment (
    EnrollmentID  INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID     INTEGER NOT NULL,
    ClassID       INTEGER NOT NULL,
    Grade         TEXT,  -- e.g., "A", "B+", or NULL if in progress
    UNIQUE (StudentID, ClassID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ClassID)   REFERENCES Class(ClassID)     ON UPDATE CASCADE ON DELETE CASCADE
);

-- Helpful indexes
CREATE INDEX IF NOT EXISTS idx_class_course   ON Class(CourseID);
CREATE INDEX IF NOT EXISTS idx_class_lecturer ON Class(LecturerID);
CREATE INDEX IF NOT EXISTS idx_enroll_student ON Enrollment(StudentID);
CREATE INDEX IF NOT EXISTS idx_enroll_class   ON Enrollment(ClassID);
"""

def main():
    with sqlite3.connect(DB) as conn:
        conn.executescript(DDL)
    print(f"Schema created in {DB}")

if __name__ == "__main__":
    main()
