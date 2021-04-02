# all
# Returns 'True' if all elements of the iterable are truthy (or if the iterable is empty)

print(all([0,1,2,3])) # False, 0 is Falsy

print(all([char for char in 'eio' if char in 'aeiou'])) # True 
# This gets the list chars 'aio' from 'aeiou', all elements are Truthy.

people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Christina']
print(all(name[0]=='C' for name in people)) # True, as all values start with 'C'


# any
# Returns 'True' if any element of the iterable is truthy, instead of all being truthy
print(all([0,1,2,3])) # True, at least 1 value is truthy

# We do not have to use the list comprehension brackets, though.
print(name[0]=='C' for name in people) # Notice there are no brackets, we are just trying to get a True/False value

# Implement a function 'is_all_strings' that accepts a single iterable and returns True if it contains ONLY STRINGS. Otherwise it should return False.
# e.x. is_all_strongs(['a', 'b', 'c']) # True

def is_all_strings(x):
  return all(type(char) == str for char in x) # returns value True or False if the type of value in each char within x is a string

is_all_strings(['a', 2, 'c'])