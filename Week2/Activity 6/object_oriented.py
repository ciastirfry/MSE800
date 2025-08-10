# Week 2 - Activity 6: Object Oriented Program using List of Object Data Types

class PersonalDetails:
    def __init__(self):
        """Initialize an empty list to store personal details."""
        self.personal_details = []

    def collect_details(self):
        """Collect name, age, and address from the user and store in personal_details list."""
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        self.personal_details = [name, age, address]

    def display_details(self):
        """Display each detail with labels."""
        print("\n--- Personal Details ---")
        print(f"Name: {self.personal_details[0]}")
        print(f"Age: {self.personal_details[1]}")
        print(f"Address: {self.personal_details[2]}")

    def update_age(self):
        """Ask how many years to add to current age, update it, and display updated info."""
        years_to_add = int(input("\nEnter number of years to add to your age: "))
        self.personal_details[1] += years_to_add
        print(f"\nAfter {years_to_add} years, {self.personal_details[0]} will be {self.personal_details[1]} years old and live at {self.personal_details[2]}.")

def main():
    """Main function to execute the program."""
    person = PersonalDetails()
    person.collect_details()
    person.display_details()
    person.update_age()

if __name__ == "__main__":
    main()
