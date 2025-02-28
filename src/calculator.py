import sys
from src.utils import add, subtract, mul, div, expo


def get_user_choice():
    """Prompt the user for an operation choice and validate input."""
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponent")

        choice = input("Enter choice (1/2/3/4/5): ").strip()
        if choice in ("1", "2", "3", "4", "5"):
            return choice
        print("Invalid choice. Please enter a number between 1 and 5.")


def get_number(prompt):
    """Prompt the user for a number and handle invalid input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """Main function for the calculator."""
    while True:
        choice = get_user_choice()

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            operation = "Addition"
        elif choice == "2":
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == "3":
            result = mul(num1, num2)
            operation = "Multiplication"
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = div(num1, num2)
            operation = "Division"
        elif choice == "5":
            result = expo(num1, num2)
            operation = "Exponentiation"

        print(f"{operation} result: {result}")

        another = input("Do you want another calculation? (y/n): ").strip().lower()
        if another != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
