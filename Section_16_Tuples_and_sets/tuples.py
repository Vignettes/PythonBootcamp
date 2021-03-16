### What is a Tuple? ###
# It's an ordered collection or grouping of items

numbers = (1, 2, 3, 4) # Notice the parenthesis 

# But, they are immutable, you cannot edit them.

x = (1,2,3)
3 in x
# x[0] = "change me!" # TypeError: tuple error does not support object assignment

alphabet = ('a', 'b', 'c', 'd')
print(alphabet) # You can print, it, but if we try to change it, we will be unable to. 

# So why use them?
# They are faster than lists, they can make your code safer from bugs (as it cannot be changed) 
# They can be used as valid keys in a dictionary. Some methods return them to you like .items()

months = ('January', 'February', 'March', 'April') # If you needed all the months in a year to not change, use a tuple.

# You can use the tuple() function to create them as well. 

# You can still access using tuple[x]
print(months[1]) # Prints February

locations = {  
    (35.6895, 39.6917): "Tokyo Office",   # Tuple string key value pairing
    (40.7128,74.0060): "New York Office",
    (37.7749, 122.4149): "San Francisco Office"
}

print(locations[35.6895, 39.6917]) # Returns Tokyo Office

# You have to use a tuple if you're using an ordered list as a key.

## How do I iterate over tuples? ##

names = ('Colt', 'Benny', 'Johnny')
for name in names: # For each name in names
    print(name) # Print the name
    
    
    
# There are only 2 tuple methods
# .count() returns the number of times a value appears in a tuple. 
x = (1,2,3,4,4)
print(x.count(4)) # Prints 2 as 4 appears 2 times. 

# .index() tells you the index a given value is found inside a tuple
t = (1,2,3,4)
print(t.index(2)) # Prints 1 as 2 is at index 1, gives first matching index