### List Methods ###

### Append ###
# adds an item we append to end of a list

first_list = [1, 2, 3, 4] #starts initial list
first_list.append(5) #appends 5 at the end
print(first_list) #prints the list


### Extend ###
# Will add all the values passed to extend

correct_list = [1, 2, 3, 4] #creates initial list
correct_list.extend([5, 7, 8]) # EXTENDS the initial list with new list values
print(correct_list) #prints the list 


### Insert ###
# insert an item at a given position

first_list = [1, 2, 3, 4] #creates the list
first_list.insert(2, 'Hi!') #adds 'hi!' at index 2
print(first_list) 

### Clear ###
#clear the entire list
first_list = [1, 2, 3 ,4]
first_list.clear() #clears all values in list
print(first_list)


### Pop ###
#removes and return the item at a given index, if no index specified removes and return last item in list
first_list = [1, 2, 3, 4]
#first_list.pop() # takes 4
first_list.pop(2) # takes 3 if code above does not run.
print(first_list)


### Remove ###
# Remove the first item from the list whose value is x, throws valueerror if the item is not found

first_list = [1, 2, 3, 4, 4, 4]
first_list.remove(2) # removes the value 2
print(first_list) # [1, 3, 4, 4, 4]
first_list.remove(4) # removes 1 instance of value 4
print(first_list) # [1, 3, 4, 4]


### Index ###
# Find the index of a given item in a list
numbers = [5, 6, 7, 8, 8]
numbers.index(6) # returns 1 for index
numbers.index(8) #returns 3 for first instance 8
numbers.index(8,3,4) # looking for 8 between index 3 and index 4


### Count ###
# accepts single input and returns the number of times it appears in list
numbers = [1, 2, 3, 4, 5, 6, 5]
number = numbers.count(5) # would return 2 for the two instances of 5
print(number)

### Reverse ###
# reverse the elements of the list (in-place)

first_list = ["Geo", "Meo", "Cleo"]
first_list.reverse() #reverses the list
print(first_list) # prints the list 

### Sort ###
#sort the items of the list (in place)
another_list = [6, 4, 1, 2, 5]
another_list.sort() #sorts it to 1, 2, 3, 4, 5 6 ASCENDING
print(another_list)

### Join ###
# takes an input such as a list, and joins them, to turn into a string
words = ['This', 'is', 'fun']
' '.join(words) # 'This is fun' joined with the ' '  between each value