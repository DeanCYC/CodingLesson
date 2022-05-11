#HW22 2D lists & nested loops
#1. two dimensional lists
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
] #create a grid = make lists as elements in a list

#for access individual element
print(number_grid[0][0]) #row 0 and column 0
print(number_grid[2][1]) #row 2 and column 1
print("\n")

#2. nested for loops
#a for loop inside a for loop
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
] 

for row in number_grid:
    for col in row: #each indiviual element inside of arrays
        print(col)
print("\n")