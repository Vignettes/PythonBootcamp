### The __name__ variable
### When run, every Python files has a __name__ variable
### If the file is the main file being run, its value is "__main__"

from say_sup import say_sup

def say_hi():
    print(f"Hi! my __name__ is {__name__}") # Hi! my __name__ is __main__
    
say_hi() # Hi! my __name__ is __main__ as this is 
say_sup() # SUP! my __name__ is say_sup

# import Revisited
# When you use import
# 1. Tries to find the module (if it fails, throws an error)
# 2. Runs the code inside of the module being imported