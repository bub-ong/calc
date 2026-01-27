class Calc:

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        if b != 0:
            return a / b
        else:
            print("The Value is Undefiend")


print("Simple Calculator".center(50, "-"))

num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

# print(" 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiplication (*) \n 4. Division (/)").lower().strip()
while True:
    choice = input(
        " 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiplication (*) \n 4. Division (/) \n Choose an Operation: ").lower().strip()

    if choice in ['1', 'add', '+']:
        print(f"{num1} + {num2} = {Calc.addition(num1, num2)}")
        break

    elif choice in ['2', 'minus', 'sub', 'subtract', '-']:
        print(f"{num1} - {num2} = {Calc.subtraction(num1, num2)}")
        break

    elif choice in ['3', 'times', 'multiply', '*']:
        print(f"{num1} * {num2} = {Calc.multiplication(num1, num2)}")
        break

    elif choice in ['4', 'divide', '/']:
        print(f"{num1} / {num2} = {Calc.division(num1, num2)}")
        break

    else:
        print("Invalid Operation")
