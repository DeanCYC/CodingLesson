#HW15 If statements & comparison
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #>= is one of comparison operators
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(300,40,5))