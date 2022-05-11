#HW23-2 Build a translator
#more efficent and better version
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #efficent
            if letter.isupper(): #show upper and lower letters based on user's input
               translation = translation + "G"
            else:
                translation = translation + "g"
            
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
print("\n")