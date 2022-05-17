#HW7 Building a basic Calculator
#Python will convert input to strings by default
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result1 = num1 + num2
print(result1)
print("\n")

#1. int = convert strings into integer number (whole number without a decimal point)
num3 = float(num1) 
num4 = float(num2)
result2 = int(round(num3)) + int(round(num4))#int can't work with the value with a decimal point
print(result2)
print("\n")

#2. float= cover strings into a number that has decimal
result3 = float(num1) + float(num2)
print(result3)
