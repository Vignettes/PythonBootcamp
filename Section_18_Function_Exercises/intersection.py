### Write a function called intersection. This function should accept two lists and return a list
### with the values that are both input lists.

# interesction([1,2,3], [2,3,4]) # return [2,3]

# flesh out intersection pleaseeeee
def intersection(a,b):
    interescted = [x for x in a if x in b]
    return interescted
    
intersection([1,2,3], [2,3,4])