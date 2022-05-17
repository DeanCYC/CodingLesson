#HW27-1 Writing files
#Writing a new file and appending onto existing files

#appending: adding will be permanently saved to the file
employee_file = open("employees.text", "a")

employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service") #\n + new info: make it shows in the new line

employee_file.close()