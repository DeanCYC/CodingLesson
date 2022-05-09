#HW20 For loop
#allow to loop over a different collections of items
#specify a variable to be used on every iteration of for loop 
#and each time most likely have a different value
#1. strings
for letter in "Giraffe Academy": #for every letter inside of giraffe academy, will be done by somthing
    print(letter) #looping though all of the letters inside of giraffe academy
print("\n")

#2. array
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
print("\n")

#3. a series of number
for index in range(10):
    print(index) #print out every number in the range from 0 to 10 but not including 10
print("\n")

#4. a range of number
for index in range(3, 10): #10 won't be included
    print(index) #print out every number in the range from 3 to 10 but not including 10
print("\n")

#5. a range of a array
friends = ["Jim", "Karen", "Kevin"]
#len(friends) = spit out three because there is three elements
for index in range(len(freinds)):
    print(friends[index])
print("\n")

#6. for specific interation
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("not first")
print("\n")