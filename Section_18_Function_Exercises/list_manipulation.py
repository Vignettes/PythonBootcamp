### Write a function called list_manipulation. This function should take in four parameteters 
### (a list, command, location, and value).
### If the command is 'remove' and the location is end, the function should remove the last value in the list.
### If the command is 'remove' and the location is 'beginning', the function should remove the first value in the list and return it.
### If the command is 'add' and the location is 'beginning' the function should add the value (4th parameter) to the begining and return the list.
### If the command is 'add' and the location is 'end' the function should add the value to the end of the list and return the list.

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(a_list, a_command, a_location, a_value=False):
    ### If the command is 'remove' and the location is end, the function should remove the last value in the list.
    if a_command == 'remove' and a_location == 'end':
        return a_list.pop()
### If the command is 'remove' and the location is 'beginning', the function should remove the first value in the list and return it.
    elif a_command == 'remove' and a_location == 'beginning':
        return a_list.pop(0)
### If the command is 'add' and the location is 'beginning' the function should add the value (4th parameter) to the begining and return the list.
    elif a_command == 'add' and a_location == 'beginning':
        a_list.insert(0, a_value)
        return a_list
### If the command is 'add' and the location is 'end' the function should add the value to the end of the list and return the list.    
    elif a_command == 'add' and a_location == 'end':
        a_list.append(a_value)
        return a_list

    

list_manipulation([1], "remove", "beginning", 20)
    