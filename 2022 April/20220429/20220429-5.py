#HW9 Lists
# #open and closed square brackets in Python is for storing a bunch of values inside of list
friends = ["Kevin", "Karen", "Jim"] #can put strings, numbers, or booleans in list
#friends = ["Kevin", 2, False] is also work
print(friends)
print("\n")


#access individual elements inside of this list: by index(start from 0)
print(friends[0])
print(friends[2])
print(friends[-1]) #use also negative index, then it starts from the back of the list
#friends = ["Kevin", "Karen", "Jim"]
#              0        1       2
#             -3       -2      -1 

#can use index to set a ranage
print(friends[1:]) #number+a colon= grab the index poistion and everything after it 
print("\n")

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[1:3]) #Karen(1), Jim(2), won't including (3)
print("\n")

#modify elements
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends[1])