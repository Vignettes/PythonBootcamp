# _name - supposed to be for internal use
# __name - Python will mangle the name behind the scenes
# __name__ - convention for Python specific methods

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!" # specifies not to be used outside the class
        self.__msg = "I like turtles"
        self.__lol = "hahahah" # creates _Person__lol
    
    
p = Person()
print(p.name) # "Tony"
print(p._secret) # "hi!"
print(p._Person__msg) # will allow us to print the __msg


