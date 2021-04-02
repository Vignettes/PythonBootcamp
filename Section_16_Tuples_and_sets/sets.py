### What is a set? ###

# Sets are like formal mathetmatical sets
# They are a collection of data that do not have duplicate values
# There are no order to them
# You cannot access items in a set by index
# They can be useful a collection of elements, but don't care about ordering, or if there are not duplicates

s = {1, 4, 5} # set of 1 4 5
s = set({1, 2, 3, 4, 5}) # you can use the set() function as well

# We can test if an element is in a set though.

print(2 in s) # True as 2 in s

# You can use a for loop to access all of them

for thing in s:
    print(thing) # 1, 2, 3, 4, 5


cities = ['Los Angeles', 'Tokyo', 'Tampa', 'Tokyo', 'Tampa', 'Boston']    
# Say we want to remove the duplicates from this
print(set(list(cities))) # Creates a set to remove the duplicates, then turns it back to a list. 

## Set methods ##
# Working with sets is very common

# We can use .add() to add data in as we go

s.add(5) # adds 5 to the set, would not allow you to add it twice
print(s) 

# We can use .remove() to remove data
s.remove(5) # Removes 5 from the set
print(s)

# We can use .discard() 
s.discard(4) # Discard will not give you an error if you try to discard the same value twice.
print(s)

# We can use .copy() to copy a set
another_s = s.copy() # Creates the copy, they would not be the same if compared from memory

# We can use .clear() to empty the set
s.clear() # Set is now empty :(
    
## Set Math ##

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

print(math_students | biology_students) # the | combines the two and the duplicates are removed
print(math_students & biology_students) # 'James' 'Matthew' as they are both in the two sets