# Week 1 - Activity 1: Factorial Calculator using `while` Loop

## Description

This Python program calculates the **factorial** of a non-negative integer provided by the user. It uses a `while` loop and includes error handling for:
- Zero input (0! = 1)
- Negative numbers (not allowed)
- Invalid (non-integer) inputs

---

## How it Works

The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`.

Examples:
- 5! = 5 × 4 × 3 × 2 × 1 = **120**
- 0! = **1** (by definition)

---

## Program Structure

The program is modularized with:

- `calculate_factorial(number)`: A function to compute the factorial using a `while` loop.
- `main()`: Handles user input, validation, and output display.
- `if __name__ == "__main__"`: Ensures proper script execution.

---

## Sample Output

```
Enter a non-negative integer: 5
The factorial of 5 is: 120
```

For invalid inputs:

```
Enter a non-negative integer: -3
Error: Factorial is not defined for negative numbers.
```

```
Enter a non-negative integer: abc
Invalid input. Please enter a valid integer.
```