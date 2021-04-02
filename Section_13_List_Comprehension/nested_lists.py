### Nested Lists ###

# Why use nested lists?
# They are great for
# - Complex data structures - matricies
# - Game boards / mazes
# - Rows and Columns for visualization, tabulation, and grouping data

import random
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[0][1]) # 2 from 1st list, 1st index

## Printing values from a nested list you will need to use two loops.

for l in nested_list: # creates a loop for each list
    for val in l: # creates a loop for each value in each list
        print(val) # prints the value from each loop
        
new_nest = [l for l in nested_list if l in nested_list]
print(new_nest)

coords = [[10.423, 9.132], [37.22, -14.092], [21.367, 32.572]]

for loc in coords: # for each list in coords list
    for coord in loc: # for each value inside each nested list
        print(coord) # print the value
        
        
### But, we have comprehension! ###

[[print(val) for val in l] for l in nested_list]
# print the variable val, for each instance of it in l, where l is the list in nested lists.


board = [[num for num in range(1,4)] for val in range(1,4)]

print(board)

i=0
while i < 100000:
    print(random.randint(0,100000))
    i += 1