# Write a function called return_day.
# This function takes in one parameter (number 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, etc).
# If the number is less than 1 or greater than 7 the function should return None

# Hint, store your days of the week in a list or dictionary

'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(a): # defining the function with parameter a
    weekdays = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4:'Wednesday', 5:'Thursday',6:'Friday',7:'Saturday'} 
    # above is the dictionary with key value being numerical to day
    days = weekdays.get(a) # variable days is equal to dictionary weekdays value passed from a (get function)
    return days if a in range(8) else None  # return the days from weekdays if it's 1-7, else return None.
    