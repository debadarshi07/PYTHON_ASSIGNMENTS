species = 'Global Species'
class Animal:
    species = 'Class Species'
    def __init__(self,species):
        self.species = species

    def displayspecies(self):
        print('Instance species: ', self.species)
        print('Class species: ', Animal.species)
        print('Global species: ', globals()['species'])


a = Animal('Instance Species')
a.displayspecies()