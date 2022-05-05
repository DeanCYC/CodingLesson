#HW16 Building a better calculator
num1 = float(input("Enter first number: ")) #receive the information from user and convert into a float
op = input("Enter operator: ") #receive the information from user
num2 = float(input("Enter second number: ")) #receive the information from user and convert into a float

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
