#HW31-2 Object Functions
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self): #check whether the particular student is on honor roll 
        if self.gpa >= 3.5:
            return True
        else:
            return False