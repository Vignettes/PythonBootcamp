#It depends on what the meaning of the word 'is' is.

#in python, == and is are very similar, but not entirely the same.

""" 
a = 1
a == 1 #True
a is 1  #True


a = [1,2,3] #a list of numbers
b = [1,2,3] 
a == b #True
a is b #False

c = b
b is c # True because it is pointing to the same value stored in memory

is is only truthy if the same value is stored in memory
"""

x = 13 
y = 13
x == y
x is y