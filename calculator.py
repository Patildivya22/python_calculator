def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero not allowed!"
    return x / y

print(" Welcome to Python Calculator")
print("Select operation:")
print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if choice == '1':
            print(f"Result: {add(num1, num2)}")

        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")

        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")

        next_calculation = input("Do you want to calculate again? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Thank you for using  Calculator ")
            break

    else:
        print("Invalid input! Please choose 1, 2, 3 or 4.")