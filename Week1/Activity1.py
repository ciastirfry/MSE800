def calculate_factorial():
    try:
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("Error: Factorial is not defined for negative numbers.")
            return

        factorial = 1
        current = number

        while current > 1:
            factorial *= current
            current -= 1

        print(f"The factorial of {number} is: {factorial}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the function
calculate_factorial()
