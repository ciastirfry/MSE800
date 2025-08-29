# Base class for all people in the university
class Person:
    def __init__(self, name, address, age, id_number):
        self.name = name
        self.address = address
        self.age = age
        self.id_number = id_number

    def display_info(self):
        return f"Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.id_number}"

# Inheritance is demonstrated below by creating child classes
# that extend the base class 'Person' and add their own specific attributes.

# Student class inherits from Person
class Student(Person):
    def __init__(self, name, address, age, id_number, academic_record):
        super().__init__(name, address, age, id_number)
        self.academic_record = academic_record

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Academic Record: {self.academic_record}"

# Academic class inherits from Person
class Academic(Person):
    def __init__(self, name, address, age, id_number, tax_code, salary):
        super().__init__(name, address, age, id_number)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Tax Code: {self.tax_code}, Salary: ${self.salary}"

# GeneralStaff class inherits from Person
class GeneralStaff(Person):
    def __init__(self, name, address, age, id_number, tax_code, pay_rate):
        super().__init__(name, address, age, id_number)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Tax Code: {self.tax_code}, Pay Rate: ${self.pay_rate}/hr"

# --- Example Usage ---
if __name__ == "__main__":
    s = Student("MJ", "456 Chicago St", 23, "S1001", "A+ in OOP")
    a = Academic("Dr. Bird", "45 Celtics Ln", 44, "A2001", "TX456", 90000)
    g = GeneralStaff("LB James", "78 Lakers Rd", 25, "G3001", "TX789", 25.50)

    print(s.display_info())
    print(a.display_info())
    print(g.display_info())
