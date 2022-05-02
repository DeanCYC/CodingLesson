#HW12 Functions
#def = create a function
def sayhi(): #all the code that comes after this line is gonna be inside of our function
    #all code that goes inside of this function need to be indented
    print("Hello User")

#the code inside of a function isn't going to get executed by default

sayhi() #calling the function to execute the code inside of the function
print('\n')

#the flow of these functions inside the program 
print("Top") #print out the word, Top
sayhi() #execute the say hi function(print("Hello User"))
print("Bottom") #print out the word, Bottom
print('\n')

#function naming rule
#1. all lower case
#2. if there are two or more words, use under space or underscore in between

#give functions information to make them more powerful => parameters
def say_hi(name): #request parameters to execute the function
    #access the parameter or variable inside of the function
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")
print('\n')

def say_hi2(name, age): #allowing this function to receive two parameters, name and age
    print("Hello " + name + " , you are " + age)

say_hi2("Mike", "35")
say_hi2("Steve", "70")
print('\n')

def say_hi3(name, age): #allowing this function to receive two parameters, name and age
    print("Hello " + name + " , you are " + str(age))

say_hi3("Mike", 35) #can pass any type of data into a function, Ex.integer
say_hi3("Steve", 70)