#HW11 Tuples
#A type of data structure = a container where we can store different values
coordinates = (4, 5) #use open closed paretheses and put the values that we would like to store
print(coordinates[0])
print(coordinates[1])
#1. tuple is immutable = can't be changed or modified
#coordinates[1] = 10 since tuple can't be changed, so this will show an error
#2. people will use tuples for data that's never going to change
coordinates2 = [(4, 5), (6, 7), (80, 34)] #create a list with a few tuples
print(coordinates2)
#3. Using more for special situations