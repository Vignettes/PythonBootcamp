### What is a function? ###
# All the built in "methods" are a special type of function
# You can define your own
# They are a process for executing a tasks
# They _can_ accept input and return an output
# Useful for executing similar procedures over and over

"""
colors = {'none',} # a new set

def add_color():  # new function add_color
    new_color= input("gib color") # asks for new color to add
    colors.add(new_color) # adds new color to the set
    print(colors) # returns the color
add_color()
"""

# Why use functions? #
   #   Stay DRY # 
   #   DON'T    #
   #   REPEAT   #
   #   YOURSELF #
   

# def name_of_function(): 

def say_hi():
    print('Hi')
    
say_hi()


def sing_happy_birthday():
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    
sing_happy_birthday()

### The magic of the return keyword ###

def print_square_of_7():
    print(7**2) 
    
print_square_of_7()

def square_of_7():
    7**2
result = square_of_7()  # This doesn't return any value out
print(result)

def square_of_7():
    return 7**2  # returns the square of 7 captured from return
result = square_of_7()  #
print(result)

# Return exits the function, meaning the function stops running


import random

def coin_flip():
    values = ['heads', 'tails'] # heads and tails values
    print(random.choice(values)) # randomly select heads or tails 
    
coin_flip()


