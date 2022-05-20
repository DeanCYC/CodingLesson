#HW32-3 Inheritance
from Chef import Chef
#If need same functions from other classes
#1. copy and past
#2. inherit from chef class
class ChineseChef(Chef): #In this ChineseChef class, it will be able to use all of the functions that are inside of Chef class

    #overwirte the function in chef class for different result
    def make_special_dish(self):
        print("The chef makses orange chicken")  

    def make_fried_rice(self):
        print("The chef makes fried rice")