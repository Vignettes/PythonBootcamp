### How do we alter the function to accept inputs? ###

def square(num): # num is the parameter, you can give it any name you want
    return num ** 2

print(square(4)) # prints 16 from squaring the parameter


def sing_happy_birthday(name):
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print(f"Happy Birthday To You {name}")
    print("Happy Birthday To You")
    
sing_happy_birthday('John') # passes 'John' as the parameter to the function.


def add(a,b): # two parameters
    return a+b 

print(add(4,3)) # 4 and 3 passed to print 7 


# Parameters vs arguments 
# parameter in decleration, argument is what is called in the execution


## Common mistakes with return ##

def sum_odd_numbrs(numbers):
    total = 0
    for num in numbers:
        if num % 2 !=0:
            total += num
        #return total # see return is within the loop
    return total # now it is in the right place

print(sum_odd_numbrs([1,2,3,4,5,6,7])) # gives you 16