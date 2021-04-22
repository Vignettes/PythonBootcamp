### We are going to make a simple ASCII art printer.

import pyfiglet # this is for the ascii art
from termcolor import colored # this is for the colors



def create_ascii():
    text = input("What do you want to print? ")
    color = input("What color do you want it in? ")
    if color not in ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']: # checks for acceptable color
        print("WRONG, changing to default") # let's the user know they are WRONG
        color = "magenta" # changes to a default color, magenta
    ascii = pyfiglet.figlet_format(text) # converts to ascii
    ascii_colored = colored(ascii, color=color) # converts ascii to user color
    print(ascii_colored) # prints the ascii in chosen color
    
create_ascii()
    
    
