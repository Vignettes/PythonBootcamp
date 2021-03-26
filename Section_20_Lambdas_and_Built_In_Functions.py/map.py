### Map is a built-in function.
### It is a standard function that accepts two arguments.
### A function, and an interable.
### Usually used with lambdas, for each value in the iterable it returns a map object
### which can be converted into another data source.

nums = [2,4,6,8,10]
double = map(lambda x: x*2, nums) # map takes this function and this nums list and calls it on each item in nums
print(double)  # returns a map object, this is something you can iterate over.
print(list(double)) # can convert that to a list afterward with list()


people = ['Darcy', 'Christina', 'Dana', 'Annabel']
peeps = map(lambda name: name.upper(), people) # the lambda makes all values uppercase
print(list(peeps)) # converts it back to list and prints

### Write a function called 'decrement_list' it should accept a single list of numbers as a parameter. 
### It should returna  copy of the list where each item has been decremented by one.
### Use map...please.
### e.x. decrement_list([1,2,3]) # [0,1,2]

def decrement_list(arr):
    return list(map(lambda a: a-1, arr)) # returns a list type, map calls the function lambda on each item in arr.

