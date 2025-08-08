# Week 2 - Activity 1: Word Guessing Game with local variables
# Student: Fredierick Saladas

import numpy as np
import random

def generate_random_word(word_list):
    return random.choice(word_list)

def initialize_display_word(word):
    return np.array(['_' for _ in word])

def ask_for_guess():
    return input("Enter a letter: ").lower()

def update_display_word(chosen_word, display_word, guess):
    updated = False
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display_word[i] = guess
            updated = True
    return updated

def is_word_guessed(display_word):
    return '_' not in display_word

def start_game():
    words_list = ['terraform', 'engineer', 'yoobee', 'software', 'keyboard', 'sugertree', 'queen', 'numpy', 'programming', 'developer']
    max_lives = 6

    chosen_word = generate_random_word(words_list)
    display_word = initialize_display_word(chosen_word)
    lives_left = max_lives

    print("Guess the word: ", ' '.join(display_word))

    while True:
        guess = ask_for_guess()
        if update_display_word(chosen_word, display_word, guess):
            print("Correct!")
        else:
            lives_left -= 1
            print("Wrong! You lost a life.")

        print("Current word: ", ' '.join(display_word))
        print(f"Lives left: {lives_left}")

        if is_word_guessed(display_word):
            print(f"\nCongratulations! You guessed the word: '{chosen_word}'")
            break
        elif lives_left <= 0:
            print(f"\nGame over! The word was: '{chosen_word}'")
            break

# Run the game
if __name__ == "__main__":
    start_game()
