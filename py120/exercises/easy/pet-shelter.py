class Shelter:
    def __init__(self):
        self.list_of_pets = {}

    def adopt(self, owner, pet):
        if owner.name in self.list_of_pets:
            self.list_of_pets[owner.name] += [f"a {pet.species} named {pet.name}"]
        else:
            self.list_of_pets[owner.name] = [f"a {pet.species} named {pet.name}"]
        owner._number_of_pets += 1

    def print_adoptions(self):
        for owner, pet in self.list_of_pets.items():
            pet_list = '\n'.join(pet)
            print(f"{owner} has adopted the following pets:")
            print(pet_list)
            print()

class Owner:
    def __init__(self, name):
        self._name = name
        self._number_of_pets = 0

    @property
    def name(self):
        return self._name
    
    def number_of_pets(self):
        return self._number_of_pets


class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name

    @property
    def species(self):
        return self._species

    @property
    def name(self):
        return self._name
    


cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")


"""
P Hanson has adopted the following pets:
a cat named Cocoa
a cat named Cheddar
a bearded dragon named Darwin

B Holmes has adopted the following pets:
a dog named Molly
a parakeet named Sweetie Pie
a dog named Kennedy
a fish named Chester

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
"""
