class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

def view_history(history):
    print("\nHistory:")
    for entry in history:
        print(entry)

def calculator():
    history = []

    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. View History")
        print("6. Quit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '6':
            break

        if choice not in {'1', '2', '3', '4', '5'}:
            print("Invalid choice")
            continue

        if choice == '5':
            view_history(history)
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        calc = Calculator()
        if choice == '1':
            result = calc.add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = calc.subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = calc.multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = calc.divide(num1, num2)
            operation = '/'

        history.append(f"{num1} {operation} {num2} = {result}")
        print("Result:", result)

calculator()
