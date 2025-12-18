print("============================")
print("Simple Calculator Application")
print("============================")
print()

# Displaying the menu options
print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

#Taking user input
opt = input("Enter your choice: ")
print()

# Taking numbers from user
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

# Performing operations based on user choice
if opt == '1':
    print("Result: ", n1 + n2)

elif opt == '2':
    print("Result: ", n1 - n2)

elif opt == '3':
    print("Result: ", n1 * n2)

elif opt == '4':
    if n2 != 0:
        print("Result: ", n1 / n2)
    else:
        print("Error: Division by zero is not allowed..!")

else:
    print("Invalid choice..!")
