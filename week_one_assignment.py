def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference between x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the quotient of x divided by y.

    If y is zero, return an error message to avoid division by zero.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    """Prompt the user to select an operation and input two numbers.

    Perform the selected operation and display the result.
    """
    # Display available operations
    print("Select operation:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")

    # Prompt user to select an operation
    operation = input("Enter operation (+, -, *, /): ")

    # Check if the selected operation is valid
    if operation in ('+', '-', '*', '/'):
        try:
            # Prompt user to enter two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            # Handle invalid numeric input
            print("Invalid input. Please enter numeric values.")
            return

        # Perform the selected operation and display the result
        if operation == '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '/':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
    else:
        # Handle invalid operation input
        print("Invalid operation. Please select +, -, *, or /.")


if __name__ == "__main__":
    calculator()
