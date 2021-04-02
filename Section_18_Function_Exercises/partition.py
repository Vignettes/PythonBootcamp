### Write a function called partition. This function accepts a list and a callback function.
### You can assume returns True or False.
### The function should iterate over each element in the list and invoke the callback function 
### at each iteration. 
### If the result of a callback function is True, the element should go into the first list (i.e. 
### 'truthy' list)
### If the result of the callback function is False, the ement should go into the second list (i.e.
### the 'Falsy' list)
### When it's finished, partition shoudl return both lists inside of one larger list, like so:
### [truthy_list, flasy_list]


def isEven(num):
    return num % 2 == 0


def partition(a, isEven):
    truthy = [num for num in a if isEven(num) == True] # Same logic as below, but split with two lists. 
    falsy = [num for num in a if isEven(num) == False]
    print([truthy] + [falsy])
    
partition([1,2,3,4], isEven) # [[2,4],[1,3]]

def partition(a, isEven):
    print([[num for num in a if isEven(num) == True], [num for num in a if isEven(num) == False]])

# Num added to list, for each num in a if result of isEven passing num is true, else add to false list. 

partition([1,2,3,4], isEven) # [[2,4],[1,3]]