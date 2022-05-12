#HW25-3 Try except
try:
    #specific ZeroDivisionError
    value = 10/0
    #specific ValueError
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid Input")