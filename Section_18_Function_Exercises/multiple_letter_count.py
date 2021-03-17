### Write a function called multiple_letter_count. This function takes in one parameter (a string) 
### and returns a dictionary with the keys being hte letters and the values being the count of the
### letter. 
### Hint: use dictionary comprehension and count()


'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(str):
    return {x:str.count(x) for x in str}    # key x with value beign count of x in string
multiple_letter_count("This")
        