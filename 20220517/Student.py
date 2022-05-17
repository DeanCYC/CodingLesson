#HW29-1 Classes & Objects
#creating a class for a student as making a student data type
#create another file: Student.py
#class: an overview of what the student data type
class Student:
    #initialize function
    def __init__(self, name, major, gpa, is_on_probation): #define what info needed for the student data type
        #self.name = an attribute of an object
        self.name = name
        #the name of the student object is equal to the name that we passed in
        self.major = major
        #the major of the student object is equal to the major that we passed in
        self.gpa = gpa
        #the gpa of the student object is equal to the gpa that we passed in
        self.is_on_probation = is_on_probation

#can use classes and objects to model anything Ex.phone