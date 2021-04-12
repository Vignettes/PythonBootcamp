### abs
### stands for absolute value. Returns the absolute value of a number. 
### The argument may be an integer or a floating point number.

print(abs(-23))

# You can import math to turn everything to float first

import math
print(math.fabs(-4)) # returns 4.0

### Sum
### takes an iterable and an optional start.
### Returns the sum of start and the items of an iterable from left to right and returns 
### the total. Start by default is 0.

print(sum([1,2,3])) # 6
print(sum([1,2,3], 10)) # 16, starts at 10 adds 1+2+3

### Round
### Round will take a number and round it to ndigits precision after the decimal point
### If ndigits is omitted or is none, it returns the nearest integer to it's input.

print(round(3.51234)) # 4
print(round(3.51234, 3)) #3.512

### Write a function called "max_magnitute" that accepts a single list full of numbers.
### It should return the magnitude of the number with the largest magnitude (furthest from
### zero).
### e.x. max_magnitude([300, 20, -900]) #900

##### I need an explanation why the below doesn't work on Udemy###
def max_magnitude(x):
    return abs(max(x))
    
print(max_magnitude([2,54,4]))
##################################################################
# The supposed correct way #
def max_magnitude(nums):
    return max(abs(num) for num in nums)

### Write a function called "sum_even_values". This function should accept a variable number 
### of arguments and return the sum of all the arguments that are divisible by 2. If
### there are no numbers divisible by 2, the function should return 0. To be clear, it accepts
### all the numbers as individual arguments.
### sum_even_values(1,2,3,4,5,6) # 12; 2+4+6=12

def sum_even_values(*nums):
    return sum(num for num in nums if num % 2 == 0)
# Return the sum of the nums if the num in nums divide by 2 == 0 (even)
sum_even_values(1,2,3,4,5,6) #12

### Write a function called "sum_floats". This function should accept a variable number
### of arguments. The function should return the sum of all the parameters that are floats.
### If there are no floats the function should return 0
### sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9

def sum_floats(*floats):
    return float(sum(num for num in floats if )))
    
