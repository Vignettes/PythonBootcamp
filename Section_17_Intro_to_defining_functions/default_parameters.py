### Default Parameters ###

def exponents(num, power):
    return num ** power # returns num raised to the power

print(exponents(4,3)) # returns 4 raised to the power 3, printed.

## print(exponents(7)) # cannot run as it is missing a positional argument 
# How can we fix this?

def exponents(num, power=2):  # sets the default for power to 2 if no value is passed to it
    return num ** power 

print(exponents(4)) # returns and prints 16 for 4 raised to the 2nd power.

## Why are default parameters useful? ##
# Allows you to be more defensive
# Avoids errors with incorrect parameters
# More readable examples! 

## What values can default parameters be? ##
# Anything...
# They can be functions, lists, dictionaries, strings, booleans


# Now let's get a little crazy with an example

def add(a,b):
    return a+b # returns a and b values after addition

def math(a,b, fn=add):
    return fn(a,b)

print(math(4,5)) # returns and prints 9, it does this by calling the fn parameter which passes the add argument to a and b in math.

def subtract(a,b): 
    return a-b # return a - b

print(math(2,2, subtract)) # return and print 2 - 2 by passing the subtract parameter to the math function replacing the add function with subtract

## If you have trouble visualizing this, check this link to walk through the above example step-by-step:
## https://bit.ly/3bV4jJj

