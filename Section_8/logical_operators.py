""" 
Logical operators are:

and - truthy if both a AND b are true
ex. 
if a and b:
    print(c)

or - truthy if either a OR b are true 
ex.
if am_tired or isbedtime:
    print("gotosleep")


not - truthy if the opposite of a is true
ex.
if not is_weekend:
    print("go to work")
"""

#AND example
age = 6

if age > 2 and age < 8:
    print("You pay child price")
    
#OR example
city = input("Where do you live?")
if city == "los angeles" or city == "san francisco":
    print("you live in california")
else:
    print("you live somewhere else")
    
#NOT example
age = 21
#2-8 2 dollar ticket 
#65 5 dollar ticket
# 10 dolalrs for everyone else

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You pay 10 dollars")
else:
    print("You are a child or senior")
    
    