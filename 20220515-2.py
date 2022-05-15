#HW27-3 Writing files
#writing:
#2. creating a new file
#text
employee_file = open("employees1.text", "w")

employee_file.write("\nKelly - Customer Service")

employee_file.close()

#html
employee_file = open("index.html", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()