### Allows you to take part of a list based on given indexs ###

# makes a new list using slices of your old list. 

#some_list[start:stop:step]   # start is starting index, stop stopping index, step the intervals

# The indext to copy from
first_list = [1, 2, 3, 4]
first_list[1:] #[2, 3, 4]
first_list[3:] # [4]

# If you enter a negative number, it will start the slice that many back from the end

first_list[-1:] # [4]
first_list[-3:] # [2, 3, 4]


## Parameters for the stop ##
# The index to copy up to (exclusive of counting)

first_list[:2] # [1,2]
first_list[:4] # [1, 2, 3, 4]


# With negative numbers, how many items to exclude from the end (i.e. indexing by counting backwards)
first_list[:-1] #[1, 2, 3]
first_list[1:-1] # [2, 3]

## Parameter the step ##
# The interval to count and interate up on per step
# Example, a step of 2 counts every other number 1, 3, 5
first_list = [1,2,3,4,5,6]
first_list[1::2]   #[2, 3]

first_list = [1,2,3,4,5,6]
# With negative numbers, reverse the order
first_list[1::-1] # [2, 1]
first_list[:1:-1] # [6, 5, 4, 3]
first_list[2::-1] # [3, 2, 1]


### TIME FOR SOME SLICE TRICKS! ###

string = "This is fun!"
print(string[::-1]) #reverses the entire string

number = [1, 2, 3, 4, 5]
number[1:3] = ['a', 'b', 'c'] #inserts 'a' 'b' 'c' where 2, 3 were at.
print(number)


