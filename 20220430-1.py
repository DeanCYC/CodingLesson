#HW10 List functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
print("\n")
#1. extend = take a list and append another list onto the end of it
friends.extend(lucky_numbers)
print(friends) #add two list together
print("\n")

#2. append = add individual elements onto at the end of the list
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Cread")
print(friends)
print("\n")

#3. insert = add value to the position of the index that you want to add
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly") #add Kelly to index 1 position
print(friends)
print("\n")

#4. remove = remove the value from the list
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim") #remove Jim from the list
print(friends)
print("\n")

#5. clear = remove all of the elements from ths list
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear() #give us an empty list
print(friends)
print("\n")

#6. pop = pop an item off this list 
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop() #got rid of the last element inside the list
print(friends)
print("\n")

#7. = figure out if a certain element was in this list
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Kevin")) #check the index of Kevin's position
print(friends.index("Oscar")) #check the index of Oscar's position
#print(friends.index("Mike")) #check the index of Mike's position, but this name is not in the this, so will show an error
print("\n")

#8. count = count the number of similar elements in the list 
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim")) #count the number of Jim in list = 2
print("\n")

#9. sort = sort this list in ascending order
lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.sort() #put the values in the list in alphabetical order
lucky_numbers.sort() #put the values in the list in ascending order
print(friends)
print("\n")

#10. reverse = reverse a list 
lucky_numbers = [42, 8, 15, 16, 23]
lucky_numbers.reverse() #reverse the order of the list
print(friends)
print("\n")

#11. copy = create another list as copy
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends2 = friends.copy() #copy the list of firends
print(friends2)
print("\n")