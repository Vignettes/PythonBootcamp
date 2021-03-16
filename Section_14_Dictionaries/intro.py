
# I have to store all this crap!
#
# Shopping Cart
#   Item
#   Item2
#       Name
#
#
# Better get out your dictionary. 
# Which consists of key-pairs.
# We use the keys to describe our data, and the values to represent our data
# Your keys and values are seperated by colons, and each pair separated by a comma
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number"
}

print(instructor[44]) # prints "my favorite number" 




# Another way of creating dictionaries is using the dict function. 
# You assing values to keys by passing in keys and values separated by an =
# another_dictionary = dict(key = 'value') would be equal to {'key':'value'}

cat2 = dict(name="kitty", age=0.5) # can pass multiple key-value pairs with commas. 
print(cat2)


# To access information in dictionaries you use

print(cat2['name']) # prints kitty from the key name in dictionary cat2

cart = [{"name": "cat litter", "quantity": 3}, {"size": "small"}] # A list that contains dictionaries
print(cart[1]['size'])  # prints the value for size from dictionary 2 as it is at index 1

# But how do I get all of the values? I need to iterate over them!

# You can use .values() to get the values
print(cat2.values())

for v in instructor.values(): # for each value in the dictionary instructor
    print(v) # print that value
    

# You can get the keys with .keys()
for v in instructor.keys():
    print(v)
    
# But I wanna get both!
# .items() passes both key and value 
print(instructor.items())

# Now iterate over both of them.
for key,value in instructor.items(): # new variables key and value, loop over each item and print key and value
    print(key,value)
    
for k,v in instructor.items(): 
    print(f"key is {k} and value is {v}") # prints the key, then the value for each pair in instructor
        


# How do we check if something is in a dictionary?
# EASY! Just use in to find the key
# "name" in instructor # would be True
print('phone' in instructor) # Prints False, it is not in instructor.

# Well what about the values?
print('Colt' in instructor.values()) # prints True as Colt is a value in that dictionaries keys. 

# Let's get down to Dictionary Methods, ok?
# .clear() - clears out the dictionary
instructor.clear() # clears the dictionary
print(instructor)

#.copy() - makes a copy of the dictionary
cart_2 = cart.copy()
print(cart_2)

#.fromkeys() - creates key-value pairs from comma separated values
# {}.fromkeys("a","b") # {'a':'b'}
# {}.fromkeys(['email'], 'unknown') # {'email': 'unknown'}
# {}.fromkeys("a",[1,2,3,4,5,]) # {'a': [1,2,3,4,5]}

# Why use fromkeys()?
# Well I want to assign some default values to all new users so.....
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown') # Creates a dictionary with the keys in the list
                                                                             # set to unknown
print(new_user)

# But I want to really GET something.
# use .get() to retrieve a key in an object and return None instead of KeyError if the key does not exist.
d = dict(a=1, b=2)
print(d.get('a')) # prints 1 from the d dictionary. 

# Need to copy a list of data over into a dictionary
game_properties = ["current_score", "high_score", "big_wins", "no_scoppies"] # list of future keys
initial_game_state = {}.fromkeys(game_properties,0) # creates variable initial_game_state, keys from game_properties, set to 0.
print(initial_game_state)


# What if I want to POP! Pop is a way to remove an item. 
# Takes the single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the 
# value corresponding to the key that was removed
d = dict(a=1,b=2,c=3)
d.pop('a') # removes and returns the valey for a
print(d) # prints {'b': 2, 'c': 3}

### WARNNG: You cannot use just dictionary.pop() like you can with list.pop() ###

# You can use .popitem()
print(initial_game_state.popitem())  # Grabs the last key-value and returns it, then removes it from the dictionary.

# We can use update to update keys and  values in a dictionary with another set of key value pairs
# first = dict(a=1,b=2,c=3,d=4,e=5)
# second = {}
# second.update(first)
# second # prints {'a':1,'b':2,'c':3,'d':4,'e':5}
# Now if we overwrite an existing key
# second['a'] = 'AMAZING!'
# We can use update again and...
# second.update(first) 
# second # now returns {'a':1,'b':2,'c':3,'d':4,'e':5} again

person = {
    "city": "Antigua"
}
person.update(initial_game_state) # adds the initial_game_state key values into the dictionary person
print(person)
