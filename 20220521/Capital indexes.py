'''
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

def capital_indexes(phrase):
    result = []
    for index, char in enumerate(phrase):
        if char.isupper(): 
            result.append(index)
    return result
    
print(capital_indexes(input("Enter a phrase: ")))