### Class Methods ###
# Class methods are methods (with the @classmethod decorator)
# that are not concerned with instances, but the class itself.

"""
###Example###

class Person():
....
    @classmethod
    def from_csv(cls, filename):
    return cls(*params)

Person.from_csv(my_csv)
"""

class User:
    active_users = 0 # exists one time, on the User class itself

    @classmethod
    def display_active_users(cls): # automatically class is passed in, so self isn't standard, use cls
        return f"There are {cls.active_users} active users"
    
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",") # takes the string and splits it
        return cls(first, last, age)
        
    
    def __init__(self, first, last, age): 
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1 # adds one more active_users
    
    def logout(self):
        User.active_users -= 1 # remove 1 active_users
        return f"{self.first} has logged out" # return whoever logged out
    
    def full_name(self):  # on itself
        return f"{self.first} {self.last}"  # return the first name and last name
    
    def is_senior(self):
        return self.age >= 65 # True or False if over age or below

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"      
    
    
user1 = User("Joe", "Biden", 100)
print(User.display_active_users())
user2 = User("Blance", "Yup", 22)
print(User.display_active_users())

tom = User.from_string("Tom,Jones,89")
print(tom.full_name()) # Tom Jones

# The method isn't particular to an instance. The @classmethod is used more rarely though.

