# file: calculator_cli.py
from calculator_backend import calculate

def main():
    print("=== SIMPLE CALCULATOR (CLI) ===")

    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Choose operation (+, -, *, /): ")

            result = calculate(a, b, op)
            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter numbers.")

        cont = input("Continue? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
