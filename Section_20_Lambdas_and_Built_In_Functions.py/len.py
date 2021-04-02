### Len
### Return the lenght (the number of items) of an object. The argument
### may be a sequence (such as a string, tuple, list, or range) or a 
### collection (such as a dictionary, set)

len('awesome') # 7
len({'a':1, 'b':2, 'c':2}) # 3

### Object Oriented Programming example using len()

class SpecialList:  # just like list, or string, we have a custom class 
    
    def __init__(self, data):
        self.__data = data
        
    def __len__(self):  # our new len returns 50 every time
        return 50
    
l1 = SpecialList([1,40,30,100])
l2 = SpecialList([])
print(len(l1)) # 50
print(len(l2)) # 50

# the default len() has been overwritten 



