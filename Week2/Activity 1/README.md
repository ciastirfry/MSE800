This is a simple command-line implementation of the word-guessing game using **Python** and **NumPy**.

## How It Works

- A random word is selected from a predefined list.
- The player guesses one letter at a time.
- Correct guesses reveal letters in the word.
- Incorrect guesses reduce the number of lives.
- The game ends when:
  - The player correctly guesses all the letters, or
  - The player runs out of lives.

## Running the Game

1. Make sure you have Python and NumPy installed:
   ```bash
   pip install numpy
   ```

2. Run the script:
   ```bash
   python word_guess.py
   ```


# Word Guessing Game (Class-based)

**Week 2 - Activity 1**  
**Student:** Fredierick Saladas  

## Features
- Class-based structure for cleaner code and easier maintenance.
- Displays the **number of characters** in the word as a clue.
- Tracks correct and incorrect guesses.
- Ends when the player guesses all letters or runs out of lives.
