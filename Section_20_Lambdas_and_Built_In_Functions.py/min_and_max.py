### Max returns the largest item in an iterable or the largest of two or more arguments

big_Num = max(3, 9)
print(big_Num) # 9

# You can do this with strings that have alphabet values like
max('a', 'b', 'c') # 'c'

### Conversely you can use Min to get the smallest
small_Num = [2, 8, 15]
print(min(small_Num)) # 2

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(min(len(name) for name in names)) # 3
# Prints the numerical value for the smallest name in names

# If we wanted the name, we can use a lambda

print(max(names, key=lambda n:len(n))) # Ollivander
# Prints the name with the longest value, from names. 
# If this is confusing check this visualization for help: https://bit.ly/39AdZaB


songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31},
]

print(min(songs, key=lambda s: s['playcount'])) # {'title': 'happy birthday', 'playcount': 1}
# Prints the song with the least number of plays in songs
# Now, let's say I only wanted the title.
title = (min(songs, key=lambda s: s['playcount']))['title']
print(title) # happy birthday

# EXTREMES EXERCISE - Using Min and Max
# Write a function called 'extremes' which accepts an iterable. It should return a tuple
# containing the minimum and maximum elements. For example:
# extremes([1,2,3,4,5]) # (1,5)

# This is one way to do it
def extremes(x):
    smallest = min(x) # variable smallest set to lowest item in x
    largest = max(x) # variable largest set to largest item in x
    return (smallest, largest) # return tuple of smallest and largest

print(extremes([1,5,6,5,48,8])) # (1, 48)

# We can simplify this further though.
def extremes2(nums):
    return(min(nums), max(nums)) # returns ths smallest value in nums, and the largest value in nums.
    