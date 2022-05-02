#HW13 Return statement
#sometime when we call a function, we actually want to get information back from that function
#return = allow python to return information from a function

def cube(num):
    num*num*num

print(cube(3)) #the information didn't back from the function
print("\n")

def cube2(num):
    return num*num*num
    #the keyword, return, breaks out of the function, which means won't execute code after this line
    print("code")
    
print(cube2(3)) #allows to return a value back to the caller
print(cube2(4)) 
print("\n")

def cube3(num):
    return num*num*num

result = cube3(4) #won't store as cube 4 but get the value that gets returned from executing that function
print(result)