### Why use modules?
### Keep Python files small
### Reuse code across multiple files by importing
### A module is just a Python file!

# There are many built-in modules

# such as random
import random

print(random.choice(["apple", "banana", "kiwi"])) # picks a random item from list

random.shuffle(["apple", "banana", "kiwi"]) # shuffle's the list randomly

# The from keyword lets you select what you import from a module
# Say we just randint from random
from random import randint # We import teh randint portion of random

print(randint(1,100)) # We don't need random.randint because we just have randint.

# Or you can rename what you import

from random import choice as pick # we would use pick as choice in our code


# Write a function that will return true if the arguments passed are Python keywords
import keyword

def contains_keyword(*args):
    return any(keyword.iskeyword(arg) for arg in args)
# return True/False if any value from args is a keyword in Python


    