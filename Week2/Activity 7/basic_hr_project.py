# Week 2 - Activity 7: Basic HR Project
# Requirements:
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details.
# Call the give_raise() method to increase an employee’s salary and display the updated amount.

# Student: Fredierick Saladas

class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        """Displays employee details."""
        print(f"Name: {self.name}")
        print(f"Job Title: {self.job_title}")
        print(f"Salary: ${self.salary:,.2f}")
        print("-" * 30)

    def give_raise(self, percentage):
        """Increases the salary by a given percentage."""
        increase_amount = self.salary * (percentage / 100)
        self.salary += increase_amount
        print(f"{self.name} received a {percentage}% raise (${increase_amount:,.2f}).")
        print(f"Updated Salary: ${self.salary:,.2f}")
        print("-" * 30)


def main():
    employees = []

    # Input details for at least two employees
    for i in range(2):
        print(f"\nEnter details for Employee {i+1}")
        name = input("Enter employee name: ")
        job_title = input("Enter job title: ")
        salary = float(input("Enter salary: "))
        employees.append(Employee(name, salary, job_title))

    # Display initial details for all employees
    print("\n=== Employee Details ===")
    for emp in employees:
        emp.display_info()

    # Give a percentage raise to each employee
    print("\n=== Applying Raises ===")
    percentage = float(input("Enter raise percentage for all employees: "))
    for emp in employees:
        emp.give_raise(percentage)

    # Display updated details
    print("\n=== Updated Employee Details ===")
    for emp in employees:
        emp.display_info()


if __name__ == "__main__":
    main()