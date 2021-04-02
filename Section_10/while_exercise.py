from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

number = randint(1,10) #creates random number

while number != 5:  #while not equal to 5
    number = randint(1,10) #create a new random number
    i += 1 #add value to i by 1
    
print(i)