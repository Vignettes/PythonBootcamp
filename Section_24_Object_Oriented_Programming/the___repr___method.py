### String representation example ###
# The __repr__ method is one of several ways to provide a nicer string representation:

class Human:
    
    def __init__(self, name="somebody"):
        self.name = name
        
    def __repr__(self):
        return self.name

dude = Human()
print(dude)
colt = Human(name="Colt Steele")
print(f"{colt} is totally rad (probably)")


# With __repr__ we can control a string


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
        
    def __repr__(self):
        return f"{self.first} is {self.age}"
    
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
    
user1 = User.from_string("Tom,Big,89")
print(user1) # Prints as a string, makes it human to read

j = User("Judy", "Steele", 18)
print(j) # When we turn something into a string repr is called.