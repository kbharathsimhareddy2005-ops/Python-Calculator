# -------------------------------
# Calculator CLI App
# -------------------------------

# Function for Addition
def add(a, b):
    return a + b


# Function for Subtraction
def subtract(a, b):
    return a - b


# Function for Multiplication
def multiply(a, b):
    return a * b


# Function for Division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Main Program
while True:

    print("\n========== CALCULATOR ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == "5":
        print("Thank you for using Calculator!")
        break

    # Check valid choice
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please try again.")
        continue

    # Taking numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform operation
    if choice == "1":
        result = add(num1, num2)
        print("Result =", result)

    elif choice == "2":
        result = subtract(num1, num2)
        print("Result =", result)

    elif choice == "3":
        result = multiply(num1, num2)
        print("Result =", result)

    elif choice == "4":
        result = divide(num1, num2)
        print("Result =", result)