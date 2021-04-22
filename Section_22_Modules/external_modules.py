### External Modules
### Built-in modules come with Python
### External modules are downloaded from the internet

### To download external modules you use pip

# The way to use pip is:
# python3 -m pip install NAME_OF_PACKAGE
# pip NAME_OF_PACKAGE works in some instances / pip3 NAME_OF_PACKAGE

# Example install termcolor
# python3 -m pip install termcolor

from termcolor import colored

#print(dir(termcolor)) 
#print(help(termcolor)) # Prints the help docs for termcolor

print(colored("We got colors", color="white", on_color="on_red", attrs=["blink"])) # Prints the text 'We got colors' in red to terminal