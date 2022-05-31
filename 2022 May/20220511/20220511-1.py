#HW23-1 Build a translator
#eample:
#Giraffe Language
#vowels -> g
#ex.1 dog -> dgg
#ex.2 cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": #if the letter is inside of the string
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
#print out the translation of whatever the user enters in
print("\n")