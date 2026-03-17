print("\n--- SIMPLE PYTHON CALCULATOR ---")

while True:
    print("\nSelect operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = input("\nEnter choice (1-5): ")

    if choice == '5':
        print("Exiting...")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {a} + {b} = {a + b}")
            elif choice == '2':
                print(f"Result: {a} - {b} = {a - b}")
            elif choice == '3':
                print(f"Result: {a} * {b} = {a * b}")
            elif choice == '4':
                if b != 0:
                    print(f"Result: {a} / {b} = {a / b}")
                else:
                    print("Error: Division by zero")
        except ValueError:
            print("Error: Please enter numeric values.")
    else:
        print("Invalid Choice. Please enter a number between 1 and 5.")