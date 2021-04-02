### Parameters ordering
### 1. Parameters
### 2. *args
### 3. default parameters
### 4. **kwargs
### If you have all of these they MUST be in this order...

def display_info(a, b, *args, instructor='Colt', **kwargs):
    return [ a, b, args, instructor, kwargs]
print(display_info(1,2,3,last_name='Steele',job='Instructor'))
# a = 1
# b = 2
# args = (3)
# instructor = 'Colt'
# kwargs = {'last_name': 'Steele', 'job': 'Instructor'}

