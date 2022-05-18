#HW31-1 Object Functions
#class function in Python: a function can be used in a class
#1. modify the objects of that class
#2. give a specific informatin about the objects

from Student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student2.on_honor_roll())