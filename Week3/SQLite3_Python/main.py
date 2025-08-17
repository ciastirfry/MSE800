from database import create_table, create_students_table, seed_students_if_empty
from user_manager import add_user, view_users, search_user, delete_user, view_students

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. View All Students")
    print("6. Exit")

def show_startup_snapshot():
    """Activity 5 requirement: display all rows from both Users and Students tables."""
    print("\n--- Startup Snapshot ---")
    users = view_users()
    print("\nUsers table:")
    if users:
        for row in users:
            print(row)
    else:
        print("(no rows)")

    students = view_students()
    print("\nStudents table:")
    if students:
        for row in students:
            print(row)
    else:
        print("(no rows)")

def main():
    # Create tables
    create_table()             # original users table
    create_students_table()    # new Students table

    # Seed Students with two rows (once)
    seed_students_if_empty()

    # Display both tables at startup per Activity 5
    show_startup_snapshot()

    # Continue with your original menu loop
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            try:
                user_id = int(input("Enter user ID to delete: "))
                delete_user(user_id)
            except ValueError:
                print("Please enter a valid integer ID.")
        elif choice == '5':
            students = view_students()
            for s in students:
                print(s)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
