#HW26-2 Reading files
employee_file = open("employees.text", "r")
#3. read individual line inside the file
print(employee_file.readline()) #reading first line
print(employee_file.readline()) #reading second line
print(employee_file.readline()) #reading thrid line

employee_file.close()