# NO TOUCHING ======================================
from random import randint
num = randint(1, 1000) #picks random number from 1-1000
# NO TOUCHING ======================================



# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
check = num % 2 #create variable to check for remainder on num 
if check == 0:
    print("even")
else:
    print("odd")




# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""" 
if num % 2 != 0:
    print("odd")
else:
    print("even") 

The above method also works by checking if num doesn't have a remainder, 
no new variable required.
"""
    
    