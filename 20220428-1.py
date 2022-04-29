#HW4 Working with strings
from cmath import phase

print("Giraffe Academy")
print("Giraffe\nAcademy") #create new line
print("Giraffe\"Academy") #escape character
print("Giraffe\Academy") #normal backslash


#creat a string variable
phrase = "Giraffe Academy"
print(phrase)

#concatenation
phrase = "Giraffe Academy"
print(phrase + " is cool")

#functions
#1.modify strings
#2.get information about strings
phrase = "Giraffe Academy"
print(phrase.lower()) #covert into lower case
print(phrase.upper()) #covert into upper case
print(phrase.isupper()) #check if a string is entirely upper case
print(phrase.upper().isupper()) #combination
print(len(phrase)) #length
print(phrase[0]) #get individual characters inside of a string, 0 means index of the character that I want to graph
#Giraffe Academy
#0123456789
print(phrase[3])
#index function:tell us where a specific character or string is located inside of our stings
print(phrase.index("G")) #0
print(phrase.index("a")) #3
print(phrase.index("Acad")) #8: where start in string
#print(phrase.index("z")) this will show error because there is no "z"
#replace
print(phrase.replace("Giraffe", "Elephant"))
