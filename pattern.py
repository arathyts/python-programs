# Week 3 - Menu Driven Python Application


# 1. Pyramid Star Pattern
def pyramid_pattern(n):
    for i in range(1, n + 1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")

        # Print stars
        for j in range(2 * i - 1):
            print("*", end="")

        print()


# 2. Inverted Number Pattern
def inverted_number_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


# 3. Recursive function to calculate sum of first N natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)


# 4. Lambda function to calculate power
power = lambda base, exponent: base ** exponent


# Main Menu
while True:

    print("\n===== MENU =====")
    print("1. Print Pyramid Star Pattern")
    print("2. Print Inverted Number Pattern")
    print("3. Calculate Sum of First N Natural Numbers")
    print("4. Calculate Power of a Number")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("Enter the number of rows: "))
        pyramid_pattern(n)

    elif choice == "2":
        n = int(input("Enter the number of rows: "))
        inverted_number_pattern(n)

    elif choice == "3":
        n = int(input("Enter a natural number: "))

        if n < 0:
            print("Please enter a positive number.")
        else:
            result = sum_natural(n)
            print("Sum of first", n, "natural numbers =", result)

    elif choice == "4":
        base = int(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))

        result = power(base, exponent)
        print(base, "raised to the power", exponent, "=", result)

    elif choice == "5":
        print("Thank you! Program exited.")
        break

    else:
        print("Invalid choice. Please try again.")