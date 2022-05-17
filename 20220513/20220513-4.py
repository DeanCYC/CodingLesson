#HW26-4 Reading files
employee_file = open("employees.text", "r")
#3. readlines with a for loop
for employee in employee_file.readlines():
    print(employee) #print each line in the file
employee_file.close()