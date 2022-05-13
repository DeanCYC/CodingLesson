#HW26-3 Reading files
employee_file = open("employees.text", "r")
#3. read individual line inside the file
print(employee_file.readlines()) #reading all lines and put inside a list
print("\n")

#print(employee_file.readlines()[1]) #access a specific line by index

employee_file.close()