# Write a function called last_element. This function takes in one parameter (a list) and returns 
# the last value in the list. It should return none if the list is empty.

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(a):
    if type(a) is list:
        if a != 0:
            return a[-1] 
        else:
            None
        
last_element([1,2,3])