### Using ** as an argument you can unpack dictionaries

def display_name(first,second):
    print(f"{first} says hello to {second}")
    
names = {"first": "Charlie", "second": "Sue"} # this is the dictionary

display_name(**names) # ** allows you to unpack the dictionary names

### Write a function called 'calculate' that accepts a list of keyword arguments
### 'make_float', a boolean which returns a float if True or an integer if False.
### 'operation', which is either 'add', 'subtract', 'multiply', and 'divide'
### 'first' which is a number, 'second', which is another number, and 'message' which is a string
###  that can be added.
### This function should return the result of actually running the specified opeation with 
### the first and second keyword arguments. The result of the operation with the 'first' and
### 'second' is an integer if the 'make_float' keyword argument is false, otherwise the
### result of the operation is a float. If a message is specified, it should return the message
### keyword argument + the result of the operation. Otherwise it should return the string 
### "The result is" joined with the result of the operation.

def calculate(**kwargs): # function accepting any number of key word arguments
    operation_lookup = { # new dictionary, with the functions add, subtract, divide, multiply
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False) # sets is_float equal to the value of 'make_float' defaults to False
    operation_value = operation_lookup[kwargs.get('operation', '')] 
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final
 
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
    
    
    
    

calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
