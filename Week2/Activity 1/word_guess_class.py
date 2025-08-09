# Week 2 - Activity 1: Word Guessing Game (Class-based)
# Student: Fredierick Saladas

import numpy as np
import random

class WordGuessingGame:
    def __init__(self):
        self.words_list = [
            'terraform', 'engineer', 'yoobee', 'software', 'keyboard',
            'sugertree', 'queen', 'numpy', 'programming', 'developer'
        ]
        self.max_lives = 6
        self.chosen_word = ""
        self.display_word = None
        self.lives_left = self.max_lives

    def generate_random_word(self):
        return random.choice(self.words_list)

    def initialize_display_word(self, word):
        return np.array(['_' for _ in word])

    def ask_for_guess(self):
        return input("Enter a letter: ").lower()

    def update_display_word(self, guess):
        updated = False
        for i, letter in enumerate(self.chosen_word):
            if letter == guess:
                self.display_word[i] = guess
                updated = True
        return updated

    def is_word_guessed(self):
        return '_' not in self.display_word

    def play(self):
        self.chosen_word = self.generate_random_word()
        self.display_word = self.initialize_display_word(self.chosen_word)
        self.lives_left = self.max_lives

        # Added clue: number of characters
        print(f"The word has {len(self.chosen_word)} characters.")
        print("Guess the word: ", ' '.join(self.display_word))

        while True:
            guess = self.ask_for_guess()
            if self.update_display_word(guess):
                print("Correct!")
            else:
                self.lives_left -= 1
                print("Wrong! You lost a life.")

            print("Current word: ", ' '.join(self.display_word))
            print(f"Lives left: {self.lives_left}")

            if self.is_word_guessed():
                print(f"\nCongratulations! You guessed the word: '{self.chosen_word}'")
                break
            elif self.lives_left <= 0:
                print(f"\nGame over! The word was: '{self.chosen_word}'")
                break

        print("GAME OVER.")


# Run the game
if __name__ == "__main__":
    game = WordGuessingGame()
    game.play()