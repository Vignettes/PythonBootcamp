### The first step to dealing with errors is understanding them.
### Here are some common ones 

# SyntaxError
# Occurs when Python encounters incorrect syntax (something doesn't parse)
# Usually due to typos or not knowing Python well enough

# def first: # SyntaxError


# NameError
# This occurs when a variable is not defined, i.e. it has not been assigned

# test # NameError: name 'test' not defined

# TypeError
# Occurs when:
# An operation or function is applied to the wrong type
# Python cannot interpret an operation on two data types

# 3 + s # TypeError: Unsupported operand type(s) for +: 'int' and 'str'

# IndexError
# Occurs when you try to access an element in a list using an invalid index 
# (i.e. one that is outside the range of the list or a string)

# ValueError
# This occurs when a built-in operation or function recieves an argument that has
# the right type but an inappropriate value:

# int("foo")
# ValueError: invalid literal for int() with base 10: 'foo'


# KeyError
# This occurs with a dictionary that does not have a specific key

# d = {}
# d["foo"] # KeyError: 'foo'

# AttributeError
# This occurs when a variable does not have an attribute

# 'awesome'.foo # AttributeError: 'str' object has no attribute 'foo'

