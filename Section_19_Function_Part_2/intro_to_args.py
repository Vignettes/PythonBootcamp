### The single star operator, *args.
### It is a special operator we can pass to function.
### Gathers remaining arguments as a tuple.
### This is just a parameter - you can call it whatever you want.

def sum_all_nums(num1, num2, num3):
    return num1+num2+num3

sum_all_nums(5,4,4)

# This works but we can explore easier ways to accomplish this. 

def sum_all_nums(*args): # Saying we can accept any number of args, puts them in a tuple
    total = 0 # new variable total set to 0
    for num in args: # for each num in args
        total += num # add the num to total
    print(total) # print the total
    
sum_all_nums(4,4,4,5) 

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args: # if the word "Colt" and "Steele" in args
        return "Welcome back Colt!" # return "Welcome back Colt!"
    return "Not sure who you are"

print(ensure_correct_info(1,True,"Steele","Colt"))

### Define a function 'contains_purple' which acepts any number of arguments. It should
### return 'True' if any of the arguments are 'purple'. Otherwise it should return 'False'
### e.x. contains_purple(25, 'purple') # True

def contains_purple(*args):
    if 'purple' in args:
        return True
    return False