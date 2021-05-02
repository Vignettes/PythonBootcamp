### Anytime we make a new instance of a class, Python looks for the __init__ method ###

# Almost any time you make a new class you should have an __init__ method. The exception is if you are making a class that only
# holds methods and no data.

class User:
    def __init__(self, first, last, age): # self keyword refers to the specific instance of this class
        # print("A NEW USER HAS BEEN MADE!") # runs each time this is initiatied 
        self.name = first
        self.last = last
        self.age = age

user1 = User("Joe", "Biden", 100)
user2 = User("Blance", "Yup", 22)

print(user1.name)
