
def main():
#calculator app
    print("Welcome to the calculator app")
    print("Select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice(1/2/3/4): ")  #user inputs their choice for calculation
    num1 = int(input("Enter first number: "))  #user inputs first number
    num2 = int(input("Enter second number: "))  #user inputs second number
    if choice == '1':
        print('Addition of two numbers is : ',num1+num2)
    elif choice == '2':
        print('Subtraction of two numbers is : ',num1-num2)
    elif choice == '3':
        print('Multiplication of two numbers is : ',num1*num2)
    elif choice == '4':
        print('Division of two numbers is : ',num1/num2)
    else:
        print("Invalid input")
        
    main()