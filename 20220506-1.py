#HW17 Dictionaries
#dictionary: a special structure in python which allows to store information
#=> key value pairs
monthConversions = { #create a dictionary inside of these open and closed curly brackets 
    "Jan": "January", #key(have to be unique): value
    "Feb": "February", #key could be strings or number
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
} 

#[]
print(monthConversions["Mar"])
print("\n")

#.get
print(monthConversions.get("Dec")) 
print(monthConversions.get("Luv")) 
print(monthConversions.get("Luv", "Not a valid Key")) #can specify a default value if the key is not found