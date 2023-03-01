# write a program for a calculator that calculates what the user wants to do

def calculate():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Root")
    print("7.Exit")
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice == '1':
        print("Addition")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 + num2)
    elif choice == '2':
        print("Subtraction")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 - num2)
    elif choice == '3':
        print("Multiplication")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 * num2)
    elif choice == '4':
        print("Division")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 / num2)
    elif choice == '5':
        print("Power")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 ** num2)
    elif choice == '6':
        print("Root")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 ** (1/num2))
    elif choice == '7':
        exit()
    else:
        print("Invalid input")
        calculate()


calculate()