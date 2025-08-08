# Week 2 - Activity 1: Word Guessing Game with Global Variables
# Student: Fredierick Saladas

import numpy as np
import random

# Global variables
words_list = ['church', 'developer', 'coffee', 'software', 'laptop']
max_lives = 6
chosen_word = ""
display_word = None
lives_left = max_lives

def generate_random_word():
    global chosen_word, display_word
    chosen_word = random.choice(words_list)
    display_word = np.array(['_' for _ in chosen_word])
    print("Guess the word: ", ' '.join(display_word))

def ask_for_guess():
    guess = input("Enter a letter: ").lower()
    return guess

def process_guess(guess):
    global display_word, lives_left

    if guess in chosen_word:
        print("Correct guess!")
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[idx] = guess
    else:
        print("Wrong guess!")
        lives_left -= 1

def check_game_over():
    global lives_left, display_word
    if '_' not in display_word:
        print(f"\nYou guessed it right! The word was '{chosen_word}'.")
        return True
    elif lives_left <= 0:
        print(f"\nYou ran out of lives. The word was '{chosen_word}'.")
        return True
    return False

def start_game():
    global lives_left
    lives_left = max_lives
    generate_random_word()
    
    while True:
        guess = ask_for_guess()
        process_guess(guess)
        print("Current word: ", ' '.join(display_word))
        print(f"Lives left: {lives_left}")
        if check_game_over():
            break
    print("GAME OVER.")

# Run the game
if __name__ == "__main__":
    start_game()