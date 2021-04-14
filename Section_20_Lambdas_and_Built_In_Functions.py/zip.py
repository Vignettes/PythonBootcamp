### zip ###
### Makes an iterator that aggregates elements from each of the iterables.
### Returns an iterator of tuples, where the i-th tuple contains the i-th element
### from each of the argument sequences or iterables.
### The iterator stops when the shortest input iterable is exhausted.

first_zip =  zip([1,2,3], [4,5,6])
list(first_zip) # [(1,4), (2,5), (3,6)] | the pairs are one from first, one from second...etc
dict(first_zip) # {1: 4, 2: 5, 3: 6}

### You can also use the * operator with zip
five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*five_by_two))) # [(0,1,2,3,4), (1,2,3,4,5)]

### Let's get jazzy with some more examples 

# We have 3 students, and their midterm and final grades. We want the highest score, but we want to do this
# dynamically.
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']
# We can combine to see all of them with the student
print(list(zip(midterms, finals, students))) # [(80, 98, 'dan'), (91, 89, 'ang'), (78, 53, 'kate')]

final_grades = [max(pair)for pair in zip(midterms, finals)]
# new variable is a list with the max value from the pair in the zip of midterms and finals
print(final_grades) # [98, 91, 89]

# But you said we needed the names!

final_grades = {t[0]:max(t[1], t[2])for t in zip(students, midterms, finals)}
# dictionary comprehension where the tuple 0 (name) is combined with the max of the other two tuples
print(final_grades) # {'dan': 98, 'ang': 91, 'kate': 78}


### Interleaving strings ###
### Write a function called 'interleave' that accepts two strings. It should return a new string
### containing the 2 strings interwoven or zipped together. For examples:
### interleave('hi, 'ha') # 'hhia'
### This might seem easy using zip, but there are a couple of intermediate steps to go from 
### zip back to a single string.
### Here is some help:
### 1. Suppose we call interleave('hi', 'no')
### 2. zip the two strings togetehr, giving you a list of tuples (once you convert from the zip_object)
### 3. For each tuple in the list, join them together using "".join, gives you a list ['hn', 'io']
### 4. Finally, joint he items in the list together using "".join again resulting in 'hnio'

def interleave(a, b):
    print(''.join(''.join(x) for x in (zip(a,b))))
# performs join twice on x in the zip of a and b
interleave('no', 'ee') # 'neoe'


### Write a function called 'triple_and_filter'. This function should accept a list of numbers,
### filter out every number that is not divisible by 4, and return a new list where every remaining
### number is tripled.
### ex. triple_and_filter([1,2,3,4]) # [12]

def triple_and_filter(*nums):
    new = [num * 3 for num in nums if num % 4 == 0]
    print(new)
    
triple_and_filter(1,5,3,8,10)

# Alternatively

def triple_and_filter(nums):
    return list(num*3 for num in nums if num % 4 == 0)


### Write a function called 'extract_full_name'. This function should accept a list of dictionaries
### and return a new list of strings with the first and last name keys in each dictionary concatenated.
### ex. names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
###     extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']

def extract_full_name(dicts):
    return [" ".join(dict.values()) for dict in dicts]
# join the dictionary values in the dictionary with space 
    
   
 
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]    
extract_full_name(names)