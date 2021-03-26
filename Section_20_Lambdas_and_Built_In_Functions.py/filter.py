### Filter ###
### There is a lambda for each value in the iterable
### Returns filter object which can be converted into other iterables
### The object contains only the values that return true to the lambda

l = [1, 2, 3, 4,]
evens = list(filter(lambda x: x % 2 == 0, l)) 
# creates a list that contains the filtered items which are 'True' from the lambda that is 
# taking an argument from l
print(evens)

# Another example would be to filter a list of names to those only starting wtih 'a'

names = ['aron', 'jim', 'anthony', 'timmy']
a_names = filter(lambda n: n[0] == 'a', names) 
# filters out 'True' values that match the lambda for first index being a within names.
print(list(a_names))


# Let's try to pull the inactive users from this dictionary
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
 
inactive_users = filter(lambda u: not u['tweets'], users) # filter for 'tweets' being empty in users 
print(list(inactive_users))


usernames = list(map(lambda user: user['username'].upper(), 
     filter(lambda u: not u['tweets'], users)))
# New variable 'usernames' contains a list where the lambda user makes the 'username' uppercase
# for records which have no tweets within the users dictionary
print(usernames)

### Combining filter and map
# Given this list of names

names = ['Lassie', 'Colt', 'Rusty']

# Return a new list with the string
# 'Your instructor is ' + each value in the array,
# but only if the value is less than 5 characters.

print(list(map(lambda name: f"Your instructor is {name}", 
    filter(lambda value: len(value) < 5, names))))
# Creates a list, based on map executing the lambda to print the instructors name, 
# which takes filtered values from names, if they are less than 5 characters in lenght.

# Why do this when we can do list comprehension
# You won't use these a lot but you should be familiar with them. If you can use list comprehension, use it.


### Write a function called 'remove_negatives' that accepts a list of numbers and returns a 
### copy of the lists with all negative numbers removed. Use filter() in your implementation,
### not a list comprehension!
### e.x. remove_negatives([-1,3,4-99]) # [3,4]

def remove_negatives(nums):
    removed = list(filter(lambda x: x >= 0, nums)) 
    # removed variable equal to a list of the true filtered results from the lambda x run on nums
    return removed

print(remove_negatives([-2,3,-4])) # prints 3