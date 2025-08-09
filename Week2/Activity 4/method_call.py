# Week 2 - Activity 4: String Manipulation without __init__

# Benefit of using __init__:
# The __init__ method is useful because it allows you to set and store 
# attributes when the object is created, eliminating the need to pass 
# the same data repeatedly to each method. This improves code readability, 
# reduces repetition, and makes the object’s state easy to manage.

class StringManipulator:
    def find_character(self, text, char):
        """
        Find the position of the given character in the text.
        Returns the index if found, else -1.
        """
        return text.find(char)

    def get_length(self, text):
        """
        Return the length of the given text.
        """
        return len(text)

    def to_uppercase(self, text):
        """
        Convert the given text to uppercase and return it.
        """
        return text.upper()

# Create an instance of the StringManipulator class
manipulator = StringManipulator()

# Sample text
text = "example"

# Find a character
result = manipulator.find_character(text, 'x')
if result != -1:
    print(f"The character was found at index {result}")
else:
    print("The character was not found in the string.")

# Get the length of the string
length = manipulator.get_length(text)
print(f"The length of the string is: {length}")

# Convert to uppercase
uppercase_text = manipulator.to_uppercase(text)
print(f"The string in uppercase is: {uppercase_text}")