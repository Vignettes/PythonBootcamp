### Dictionary Comprehension ###

# The syntax is {____:____ for ____ in ____}
# Iterates over keys by default.
# Can use .values() to iterate over keys and values

numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()} # times the values by 2 
print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}

new_num = {num: num**2 for num in [1,2,3,4,5]} # Create new dictionary and square the values from dictionary
print(new_num)  # ['1': 1, '2': 4, '3': 9, etc.]

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))} # key of str1, value of str2 for the length of str1
print(combo) # {'A': '1', 'B': '2', 'C': '3'}


instructor = {
    "name": "Colt",
    "owns_dog": "yes",
    "num_courses": "4",
    "favorite_language": "Python", 
}

yelling_instructor = {k.upper(): v.upper() for k,v in instructor.items()} # for each key and value in instructor print as uppercase
print(yelling_instructor)


num_list = [1,2,3,4]
listthis = { num:("even" if num % 2 == 0 else "odd") for num in num_list} # for each number print even or odd 
print(listthis)

# Turn the following lists into key value paired dictionary. 
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(len(list1))}

# Turn the following into a dictionary

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = dict(person) # Ta-da

# You can also do (Dictionary Comprehension):
answer = {thing[0]: thing[1] for thing in person}

# Or (No references to indexes)

answer = {k: v for k,v in person}

answer = {k: 0 for k in ['a', 'e', 'i', 'o', 'u']}
print(answer)


# Loop over all the characters  65-90 and give the corresponding ACII character
answer = {chr(i):i for i in range(65,91)}
print(answer)