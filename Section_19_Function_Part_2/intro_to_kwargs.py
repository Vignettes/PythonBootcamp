### **kwargs stands for keyword arguments.
### Special operator we can pass to functions
### Gathers remaining keyword arguments as a dictionary
### This is just a parameter - you can call it whatever you want

def fav_colors(**kwargs):
    print(kwargs)
    
fav_colors(george='red', tim='blue') # gives you a dictionary with {'george': 'red', 'tim': 'blue}


# Let's turn it into a way to print people's favorite colors.
def fav_colors(**kwargs):
    for person, color in kwargs.items(): # for each person and color in kwargs.items() 
        print(f"{person}'s favorite color is {color}") # print the name and favorite color

fav_colors(george='red', tim='blue')

### kwarg exercise time. 
### Write a function called 'combine_words' which accepts a single string called word
### and any number of additional key word arguments. If a prefix is provided, return the 
### prefix followed by the word. If a suffix is provided, return the word followed by the suffix. 
### If neither is provided, just return teh word. 
### e.x. combine_words('child' prefix='man') # manchild

def combine_words(word, **kwargs):  # word and **kwargs provided in function
    for fix, value in kwargs.items(): # for fix (the key) and value (the value) in the dictionary kwargs
        if  fix == 'prefix': # if prefix present
            return value + word # return the value before the word
        elif fix == 'suffix': # if suffix present
            return word + value # return the word then the value
    return word # else just return the word
    
print(combine_words('red', prefix='man'))

### This can also be done as....

def combine_words(words, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word