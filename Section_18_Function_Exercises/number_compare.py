### Write a function called number_compare. It should take in two parameteres (both numbers). If this first is 
### greater than the second, this function returns "first is greater". If the second number is greater than the first,
### the function retuns "Second is greater". Otherwise returns "Numbers are equal".

'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    return "Numbers are equal"

number_compare(1,5)