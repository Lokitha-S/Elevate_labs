def add(a, b=0):
    return a + b

def subtract(a, b=0):
    return a - b

def multiply(a, b=1):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def display_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Select operation (1-5): ")

    if choice == '5':
        print("Exiting... Happy Coding!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number (or press Enter for default): ") or "None")
            
            if num2 == "None":
                if choice == '1': print(f"Result: {add(num1)}")
                elif choice == '2': print(f"Result: {subtract(num1)}")
                elif choice == '3': print(f"Result: {multiply(num1)}")
                else: print("Error: Division requires two numbers.")
            else:
                n2 = float(num2)
                if choice == '1': print(f"Result: {add(num1, n2)}")
                elif choice == '2': print(f"Result: {subtract(num1, n2)}")
                elif choice == '3': print(f"Result: {multiply(num1, n2)}")
                elif choice == '4': print(f"Result: {divide(num1, n2)}")
        
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid Choice. Please try again.")