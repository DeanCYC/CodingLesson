#HW29-1 Classes & Objects
#creating a class for a student as making a student data type
#create another file: Student.py
#class: an overview of what the student data type
class Student:
    #initialize function
    def __init__(self, name, major, gpa, is_on_probation): #define what info needed for the student data type
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation