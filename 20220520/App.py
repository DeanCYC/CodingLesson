#HW32-1 Inheritance
#Define a bunch of attributes and functions and things inside of a class
#then can create another class and can inherit all of those attributes

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
#myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
