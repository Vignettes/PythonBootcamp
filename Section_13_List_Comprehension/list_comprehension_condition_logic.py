### You can use conditional logic within the comprehension ###

numbers = [1, 2, 3, 4, 5, 6]

# loop over each num value in numbers, if it is divisible 
# by 2 with 0 remainder add to even list.
evens = [num for num in numbers if num % 2 == 0]  


# loop over each num value in numbers, if it divides into
# 2 with a remainder, add to odd list.
odds = [num for num in numbers if num % 2 != 0]


print(evens)
print(odds)

### Adding else statements ###

#takes even numbers and multiplies by 2, if they are odd, divide by 2
elsed = [num*2 if num % 2 ==0 else num/2 for num in numbers] 
print(elsed)
### Adding not in ###

with_vowels = "This is so much fun!"
#For each character in with_vowels if the value is NOT in "aeiou" as a string because of .join
without_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(without_vowels)




# Given a list of values Elie, Tim, Mat take only the 1st letter from each name to a new list.

names = ['Elie', 'Tim', 'Matt']
answer = [name[0] for name in names] # variable at 0 index for each value in names
print(answer)

# Now imagine you have a list of numbers 1-6. Tell me the even ones in a new list.

numbers = [1,2,3,4,5,6]
answer_2 = [num for num in numbers if num % 2 == 0] # add variable if the variable in numbers is divisibel by 2 with 0 remainder

print(answer_2)


list_1 = [1,2,3,4]
list_2 = [3,4,5,6]

answer = [num for num in list_1 if num in list_2] # new variable num added if value for num in list_1 if value in list_2
print(answer)


names = ['Elie', 'Tim', 'Matt']

answer2 = [char[::-1].lower() for char in names] # New variable character, reversed to lowercase, for each variable in names.
print(answer2)


# For all numbers between 1 and 100, including 100, create a variable called answer, which contains a list with all the numbers that are divisble by 12.

list = range(1,101) # creates a list with range 1-100
answer =  [num for num in list if num % 12 == 0] # creates variable, if variable from list divisible by 12 with 0 remainder
print(answer)

## This can also be done as

answer = [val for val in range(1,101) if val % 12 == 0] # Same logic as above but it combines the range into the list
print(answer)


### Given the strong 'amazing', create a variable called answer, which is a list containing all the letters 'amazing' but not the vowels (a,e,i,o, and u). 
### The answer should look like ['m','z','n','g']

answer = [char for char in "amazing" if char not in "aeiou"] # New variable char created for each character in 'amazing' if that character is not in 'aeiou'
# God I love Python, just look at that logic. God damn. 
print(answer)