### Class Attributes ###
# Defined once
# We can only define attributes directly on a class that are shared by all instances of
# a class and the class itself.

class User:

    active_users = 0 # exists one time, on the User class itself

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

print(User.active_users) # 0

user1 = User("Joe", "Biden", 100)
user2 = User("Blance", "Yup", 22)

print(User.active_users) # 2, prints directly from the User class attribute

print(user2.logout()) # Blance logged out
print(User.active_users) # We now have 1 active user