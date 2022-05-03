#HW14-2 If statements
#if statements
is_male = True #create a boolean variable
#can use if statement to cheak to see what the value of this variable is and if it's true then can do something
if is_male: #the value has to be able to be reducible to a true or false value
    #anything that put below this with and indentation is going to be executed when that conditions true
    print("You are a male")
#change is_male = False 
#then won't print out anything
print("\n")

#else
is_male2 = False

if is_male2: 
    print("You are a male")
else:
    print("You are not a male")
print("\n")

#or
is_male3 = False
is_tall = False

if is_male3 or is_tall: #either male or tall (will execute when one or both are true)
    print("You are a male or tall or both")
else:
    print("You neither male nor tall") #both conditions are false
print("\n")

#and
is_male4 = True
is_tall2 = True

if is_male4 and is_tall2: #male and also tall (will execute when both are true)
    print("You are a tall male")
else:
    print("You are either not male or not tall or both") #one of condition or both conditions are false
print("\n")

#elif = else if
is_male5 = False
is_tall3 = False

if is_male5 and is_tall3: #male and also tall (will execute when both are true)
    print("You are a tall male")
elif is_male5 and not(is_tall3): #not() = negate anything in ()
    print("You are a short male")
elif not(is_male5) and is_tall3: 
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall") #one of condition or both conditions are false
print("\n")