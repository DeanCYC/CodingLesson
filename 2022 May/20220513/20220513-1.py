#HW26-1 Reading files
#Reading external files(Ex.CSV, HTML) in Python
#mode
#1. r = Read:reading information in the file (get info)
#2. w = Write:change infirmation in the file (modify info)
#3. a = Append:append information onto the end of the file (only add new info)
#4. r+ = Read and Write

#open("employees.text", "r") #(Path to the file or File name, mode)

#function
employee_file = open("employees.text", "r") #store the opened file inside of a variable
#1. check if the file is readable
print(employee_file.readable())
print("\n")
#2. spit out all function in the file
print(employee_file.read())
print("\n")
employee_file.close()