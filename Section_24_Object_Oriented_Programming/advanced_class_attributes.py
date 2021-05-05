# You can access the instances version of allowed, but it will just be a copy.


class Pet:

    allowed = ['cat', 'dog', 'fish', 'rat'] # these are our allowed pets
    
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
    
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species
        

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
# unallowed = Pet("James", "snake")



