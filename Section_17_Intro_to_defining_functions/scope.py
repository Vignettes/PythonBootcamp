### Scope ###

# There are rules that govern where your variables can be accessed, thus you should know about scope

# Variables created in functions are scoped in that function
# Meaning that variable can ONLY be used within that function
# Example below of one created outside the function, making it within global scope

instructor = 'Colt'

def say_hello():
    return f'Hello {instructor}'

say_hello()

# Example below is local scope

def say_hello():
    instructor = 'Colt' # Variable is defined within the function, creating a local scope variable
    return f'Hello {instructor}'

say_hello()

print(instructor) # when you try to call this later, the variable is not accessible outside the function


## But wait, there is more! ##
# Let's try and edit a global variable inside a function

""" 
total = 0
def increment():
    total += 1
    return total

increment()  # Gives you the following error: UnboundLocalError: local variable 'total' referenced before assignment
"""

## Ok, but how can we get around this issue?
# Let's try the global keyword

total = 0
def increment():
    global total  # We're saying when we use the total variable name, we are referring to the global variable total (must happen first)
    total += 1
    return total

increment()


## Nonlocal will let you modify a parent's variable in a child (aka nested) function

def outer():
    count = 0 # setting variable count to 0
    def inner():
        nonlocal count # setting count as nonlocal, meaning it is not defined in inner, or global scope, but the variable is defined in a nested area
        count += 1
        return count
    return inner()