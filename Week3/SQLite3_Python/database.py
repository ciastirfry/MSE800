import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    """Create original users table."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# ===== Activity 5 additions =====
def create_students_table():
    """Create Students table with Stu_ID, Stu_name, Stu_address."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            Stu_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Stu_name TEXT NOT NULL,
            Stu_address TEXT
        )
    ''')
    conn.commit()
    conn.close()

def seed_students_if_empty():
    """Insert two sample rows into Students if table is empty."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Students")
    (count,) = cursor.fetchone()
    if count == 0:
        cursor.executemany(
            "INSERT INTO Students (Stu_name, Stu_address) VALUES (?, ?)",
            [
                ("Mike Jordan", "15 Goat St"),
                ("Lebron Curry", "29 Kings Ave"),
            ]
        )
        conn.commit()
    conn.close()
