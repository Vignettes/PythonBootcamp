# You can use Try and Except to try to do something, and if it doesn't work follow the except

try:
    foobar
except NameError as err:
    print('Problem!')
print('after the try')
# Problem
# after the try

# Why not try to catch them all?

try:
    colt
except: # Should put an error type there
    print('You tried to use a variable that was never declared')

# What we are doing here is catching EVERY error, which means
# we are not able to correctly identify 'what' went wrong.
# It is highly discouraged to do this.




def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d = {"name": "Ricky"}    
get(d, "name")