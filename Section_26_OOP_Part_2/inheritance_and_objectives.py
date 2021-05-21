### Inheritance

# A key feature of OOP is the ability to define a class which inherits from another class 
# (a "base" or "parent" class).

# In Python, inheritance works by passing the parent class as an argument to the definition of a child class:

class Animal:
    cool = True
    
    def make_sound(self, sound):
        print(sound)
        
    
class Cat(Animal): # Cat is inheriting from the Animal class
    pass

a = Animal()
a.make_sound("CHIRP")

blue = Cat()
blue.make_sound("MEOW")
print(Cat.cool)
print(Animal.cool)

print(isinstance(blue, Cat))

