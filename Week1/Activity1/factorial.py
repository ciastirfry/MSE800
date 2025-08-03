def calculate_factorial(number):
    if number < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None

    factorial = 1
    current = number

    while current > 1:
        factorial *= current
        current -= 1

    return factorial

def main():
    try:
        user_input = int(input("Enter a non-negative integer: "))
        result = calculate_factorial(user_input)

        if result is not None:
            print(f"The factorial of {user_input} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Entry point of the program
if __name__ == "__main__":
    main()
