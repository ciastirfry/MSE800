import sqlite3
import random
from faker import Faker
import time


class Database:
    def __init__(self, db_path="app.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()


class UserService:
    def __init__(self, db: Database):
        self.db = db

    def get_user(self, user_id):
        cur = self.db.get_cursor()
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cur.fetchone()


class OrderService:
    def __init__(self, db: Database):
        self.db = db

    def get_orders(self, user_id):
        cur = self.db.get_cursor()
        cur.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        return cur.fetchall()


class UserServiceOld:
    def get_user(self, user_id):
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result


class OrderServiceOld:
    def get_orders(self, user_id):
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result


def init_db(db: Database):
    fake = Faker()
    cur = db.get_cursor()
    cur.execute("DROP TABLE IF EXISTS orders;")
    cur.execute("DROP TABLE IF EXISTS users;")

    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product TEXT NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    users = [(fake.name(), fake.unique.email()) for _ in range(100)]
    cur.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

    for user_id in range(1, 101):
        for _ in range(random.randint(1, 5)):
            product = fake.word().capitalize()
            amount = round(random.uniform(10, 500), 2)
            cur.execute(
                "INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)",
                (user_id, product, amount)
            )
    db.commit()
    print("Database initialized with 100 users and random orders.")


def benchmark_old_service(iterations=1000):
    user_service = UserServiceOld()
    order_service = OrderServiceOld()

    start = time.perf_counter()
    for _ in range(iterations):
        user_service.get_user(1)
        order_service.get_orders(1)
    end = time.perf_counter()

    print(f"[OLD] {iterations} iterations took: {end - start:.4f} seconds")


def benchmark_new_service(iterations=1000):
    with Database("app.db") as db:
        user_service = UserService(db)
        order_service = OrderService(db)

        start = time.perf_counter()
        for _ in range(iterations):
            user_service.get_user(1)
            order_service.get_orders(1)
        end = time.perf_counter()

    print(f"[NEW] {iterations} iterations took: {end - start:.4f} seconds")


if __name__ == "__main__":
    # Run once to seed the DB
    with Database("app.db") as db:
        # Uncomment below only once to seed
        init_db(db)
        pass

    ITER = 1000
    benchmark_new_service(ITER)
    benchmark_old_service(ITER)
