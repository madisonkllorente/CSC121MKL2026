#10.6 Addition MKL
while True:
    try:
        num1 = input("Enter first number (or 'quit'): ")

        if num1.lower() == 'quit':
            break

        num2 = input("Enter second number: ")

        total = int(num1) + int(num2)
        print(f"The sum is: {total}")

    except ValueError:
        print("Oops! Please enter valid numbers only.")