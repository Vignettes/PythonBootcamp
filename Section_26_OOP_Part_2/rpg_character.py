# Let's pretend we're making an RPG. 
# Define a base class "Character" with the following properties
# 1. name - string
# 2. hp - an intger for health
# 3. level - an integer for level

# Define a subclass NPC which inherits from Character and has additional instance method called speak
# which prints the speech they would say when interacted with 


class Character:
# Define a base class "Character" with the following properties
# 1. name - string
# 2. hp - an intger for health
# 3. level - an integer for level
    def __init__(self, name, hp, level):
        self.name = name
        self. hp = hp
        self.level = level

class NPC(Character):
# Define a subclass NPC which inherits from Character and has additional instance method called speak
# which prints the speech they would say when interacted with 
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
    
    def speak(self):
        return "{0} says: 'I heard monsters running around last night!'".format(self.name)
        

char_1 = NPC("James", 20, 12)
print(char_1.speak())
char_1.hp