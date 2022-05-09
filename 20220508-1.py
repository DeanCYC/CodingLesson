#HW19 Building a guessing game
#Idea: Specify lake a secret word, and user can interact with the program and try to guess it

secret_word = "giraffe" #a secret word variable
guess = "" #a variable to store user's guess
guess_count = 0 #tack of how many times the user had guessed the word
guess_limit = 3 #set a limit on the number of guesses that user can have
out_of_guesses = False #check whether or not they have some guesses left

#prompt the user to input the secret word and keep trying
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit: #check the number of guesses
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True #True means there is no more guess

if out_of_guesses:
    print("Out of Guessess, YOU LOSE!") #1. user ran out of guesses
    print("\n")
else:
    print("You win!") #2. user guessed correctly
    print("\n")
        print("\n")