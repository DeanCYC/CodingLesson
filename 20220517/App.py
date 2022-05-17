#HW29-2 Classes & Objects
#Object: an actual student with student data type
from Student import Student #Referring to the file and referring to actual student class

student1 = Student("Jim", "Business", 3.1, False) #create a student
#class is like an overall template and it defiens what a student is
#object is an instance of a class with actual information for a student

print(student1.name)