### Instance Methods ###
#

class User:
    def __init__(self, first, last, age): 
        self.first = first
        self.last = last
        self.age = age
    
    def full_name(self):  # on itself
        return f"{self.first} {self.last}"  # return the first name and last name
    
    def is_senior(self):
        return self.age >= 65 # True or False if over age or below

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"            

user1 = User("Joe", "Biden", 100)
user2 = User("Blance", "Yup", 22)

print(user1.full_name()) # Joe Biden
print(user1.is_senior()) # True
print(user2.birthday()) # Happy 23th, Blance.


# Make a bankaccount class, that has a balance auto set to 0, and an owner.
# You should be able to withdraw and deposit, and show the new balance afterward.

class BankAccount:
    def __init__(self, owner, balance=0): 
        self.owner = owner
        self.balance = balance 
        
    def deposit(self, add):
        self.balance += add
        return self.balance

    def withdraw(self, remove):
        self.balance -= remove
        return self.balance
    
acct = BankAccount("Darcy", 3000)
print(acct.owner) # Darcy
print(acct.withdraw(300)) # 270