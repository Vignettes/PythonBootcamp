### Properties

class Human:
    def __init__(self,first, last, age):
        self.first = first
        self.last = last
        if age >= 0: # if age lower than 0
            self._age = age 
        else: # set it to 0
            self._age = 0
            
    """def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0
         """
         

    @property # a decorator and then method to be able to call later
    def age(self):
        return self._age
        
    @age.setter  # setter allow you to edit
    def age(self, value): # accepts new value
        if value >= 0: # if greater than 0 or equal
            self._age = value # update the value
        else:
            raise ValueError("age can't be negative")
        
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
            
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ") # takes the name and splits it between break
            
jane = Human("Jane", "Goodall", -9)
""" print(jane.get_age()) # returns 0 as the age is negative
jane.set_age(45)
print(jane.get_age()) # 45 """

print(jane.age)
jane.age = 20 # changes age to 20
print(jane.age) # 20
jane.full_name
jane.full_name = "John Smith"
print(jane.full_name) # name is now John Smith