### Keyword Arguments ###

# If you need to use the arguments out of their standard order you can do that the following way

def full_name(first, last):
    return f"Your name is {first} {last}"

full_name(first='Colt', last='Steele') 

print(full_name(last='Steele', first='Colt')) # by using keyword arguments you can alter the order, see last comes before steele in this example. 

## Why use keyword arguments? ##
# You may not see the value now, but it is useful when passing a dictionary to a function and unpackign it's values.

# They different from default parameters. 
# When you define a function and put the = in the parameter, you are invoking a default parameter
# When you put an = in the keyword argument you are NOT using default parameters

