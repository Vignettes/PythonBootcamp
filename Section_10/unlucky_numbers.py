#for 4 and 13 print x is unlucky
#for even print x is even
#for odd print x is odd


""" import random

x = random.randint(1,100)  #creates random number between 1, 99
print(x)

 
for num in range(x): 
    if num % 2 == 0:  
         print(f'{num}, is even')
    else:
         print(f'{num}, is odd')
    if num == 4 or num == 13:
         print(f'{num}, that is unlucky')  """
 
 
for num in range(1,21): 
    if num == 4 or num == 13:
        print(f'{num}, that is unlucky')
    elif num % 2 == 0:  
        print(f'{num}, is even')
    
    else:
        print(f'{num}, is odd')
    