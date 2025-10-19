

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return " Cannot divide by zero!"
    return a / b


def main():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        choice = input("Enter choice (1/2/3/4): ")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(f" Result: {add(a, b)}")
        elif choice == '2':
            print(f" Result: {subtract(a, b)}")
        elif choice == '3':
            print(f" Result: {multiply(a, b)}")
        elif choice == '4':
            print(f" Result: {divide(a, b)}")
        else:
            print(" Invalid choice!")
    except ValueError:
        print(" Please enter valid numbers!")


if __name__ == "__main__":
    main()
