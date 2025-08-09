# Week 2 - Activity 3: Search for a character in a string using Class
# Extended with methods to get length and convert to uppercase

class StringManipulator:
    def __init__(self, text):
        """Initialize the StringManipulator with the given text."""
        self.text = text

    def find_character(self, char):
        """
        Find the position of the given character in the text.
        Returns the index if found, else -1.
        """
        return self.text.find(char)

    def get_length(self):
        """
        Return the length of the stored text.
        """
        return len(self.text)

    def to_uppercase(self):
        """
        Convert the stored text to uppercase and return it.
        """
        return self.text.upper()

# Create an instance of the StringManipulator class
name = StringManipulator("example")

# Find a character
result = name.find_character('x')
if result != -1:
    print(f"The character was found at index {result}")
else:
    print("The character was not found in the string.")

# Get the length of the string
length = name.get_length()
print(f"The length of the string is: {length}")

# Convert to uppercase
uppercase_text = name.to_uppercase()
print(f"The string in uppercase is: {uppercase_text}")