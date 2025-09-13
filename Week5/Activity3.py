# Base class for all people in the university
class Person:
    def __init__(self, name, address, age, id_number):
        self.name = name
        self.address = address
        self.age = age
        self.id_number = id_number

    def display_info(self):
        return f"Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.id_number}"

    def greet(self):
        print(f"Hello from {self.name} at the University.")

# Student class inherits from Person and overrides methods
class Student(Person):
    def __init__(self, name, address, age, id_number, academic_record):
        super().__init__(name, address, age, id_number)  # Call to parent class initializer
        self.academic_record = academic_record

    def display_info(self):  # Method overriding
        base_info = super().display_info()
        return f"{base_info}, Academic Record: {self.academic_record}"

    def greet(self):  # Overriding greet method
        print(f"Greetings and felicitations from the student {self.name}!")

# Academic class inherits from Person and overrides methods
class Academic(Person):
    def __init__(self, name, address, age, id_number, tax_code, salary):
        super().__init__(name, address, age, id_number)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Tax Code: {self.tax_code}, Salary: ${self.salary}"

    def greet(self):
        print(f"Good day from Professor {self.name}.")

# GeneralStaff class inherits from Person and overrides methods
class GeneralStaff(Person):
    def __init__(self, name, address, age, id_number, tax_code, pay_rate):
        super().__init__(name, address, age, id_number)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Tax Code: {self.tax_code}, Pay Rate: ${self.pay_rate}/hr"

    def greet(self):
        print(f"Hello from staff member {self.name}, how can I help?")

# --- Example Usage ---
if __name__ == "__main__":
    s = Student("MJ", "644 Chicago St", 23, "S1001", "A+ in OOP")
    a = Academic("Dr. Bird", "76 Nest Ln", 11, "A2001", "TX456", 90000)
    g = GeneralStaff("LB James", "98 Kings Rd", 24, "G3001", "TX789", 25.50)

    # Display Information
    print(s.display_info())
    print(a.display_info())
    print(g.display_info())

    # Demonstrate Method Overriding
    s.greet()
    a.greet()
    g.greet()
