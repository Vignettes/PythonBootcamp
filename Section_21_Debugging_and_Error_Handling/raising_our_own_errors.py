### Raise your own exception!

# In Python we can also throw errors using the raise keyword.
# This is helpful when creation your own kinds of exception and error message.

# raise ValueError('invalid value')

def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")    
    if type(text) is not str:
        raise TypeError("text must be a string")
    if color not in colors:
        raise ValueError("must be a color")
    print(f"Printed {text} in {color}")
    
colorize('words', 'green')
colorize(5, 'red') # TypeError: text must be a string

