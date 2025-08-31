import random

# Superclass: Color
class Color:
    def __init__(self, color_name):
        self.color_name = color_name

    def describe(self):
        return f"The color is {self.color_name}."

# Subclass: TransparentColor inherits from Color
class TransparentColor(Color):
    def __init__(self, color_name, transparency_level):
        super().__init__(color_name)
        self.transparency_level = transparency_level

    def describe(self):
        return f"The color is {self.color_name} with {self.transparency_level}% transparency."

# Animal class uses Color or TransparentColor
class Animal:
    def __init__(self, species, color: Color):
        self.species = species
        self.color = color

    def describe(self):
        return f"{self.species} - {self.color.describe()}"

# --- Example Usage ---
if __name__ == "__main__":
    # Pool of animals and colors
    solid_animals = [
        ("Lion", "Golden Yellow"),
        ("Elephant", "Grey"),
        ("Tiger", "Orange"),
        ("Zebra", "Black & White"),
        ("Flamingo", "Pink"),
        ("Panda", "White and Black"),
        ("Peacock", "Turquoise"),
        ("Parrot", "Green"),
        ("Cheetah", "Yellow with Spots"),
        ("Giraffe", "Tan"),
    ]

    transparent_animals = [
        ("Jellyfish", "Blue", 70),
        ("Glass Frog", "Green", 50),
        ("Sea Angel", "Clear", 90),
        ("Icefish", "White", 60),
        ("Salp", "Clear", 80),
    ]

    # Create instances
    zoo_animals = []

    for species, color_name in solid_animals:
        color = Color(color_name)
        animal = Animal(species, color)
        zoo_animals.append(animal)

    for species, color_name, transparency in transparent_animals:
        color = TransparentColor(color_name, transparency)
        animal = Animal(species, color)
        zoo_animals.append(animal)

    # Print descriptions
    for animal in zoo_animals:
        print(animal.describe())
