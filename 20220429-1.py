#HW5 Working wiht numbers
print (2) #number
print (2.0987) #decimal number
print (-2.0987) #negative
print (3 + 4.5) #basic arithmetic,+ addition
print (3 - 4.5) #- subtraction
print (3 * 4.5) #* multiplication
print (3 / 4.5) #/ dividation

print(3 * 4 + 5) #use parentheses
print(3 * (4 + 5))

#modulates operator
print(10 % 3) #read as: ten mod three #get the remainder

#can set numbers inside of variables
my_num = 5
print(my_num)
#convert number into a string
my_num = 5
print(str(my_num)) #handy when want to print out number alongside string
print(str(my_num) + " is my favorite number")
#print(my_num + " my favorite number") will show an error

#number function could perform an operation like mathematical operation on number or give information about number
#1. abs = get absolute value
my_num = -5
print(abs(my_num))
#2. pow = allow to pass two pieces of information: number & the power that want to take the number
print(pow(3, 2)) #= 3 ^ 2
print(pow(4, 6)) #= 4 ^ 6
#3. max = return the biggest number from what we pass to it
print(max(4, 6))
#4. min = return the biggest number from what we pass to it
print(min(4, 6))
#5. round= allow to round a number as standard rounding rules
print(round(3.2))
print(round(3.7))

#Python can import external code into our file
from math import * #give us access to a lot more math functions
#6. floor = grab the lowest number (chop off the decimal point)
print(floor(3.7))
#7. ceil = grab the biggest number (round the number up)
print(ceil(3.7))
#8. sqrt = return the quare root of a number
print(sqrt(36))
