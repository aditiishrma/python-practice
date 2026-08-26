# TYPES OF INHERITANCE IN PYTHON :
# 1. SINGLE INHERITANCE
    # It is a type of inheritance where a single child class inherits the properties & methods from a single parent class.

class Animal :
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def make_sound(self):
        print(f"The Animals {self.name} produces different sounds according to their species {self.species} ")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
    def make_sound(self):
        print(f"Barkkkk!!! {self.breed}")
d = Dog("Tommy","Bhaw")
d.make_sound()
a = Animal("Leopard","Cat")
a.make_sound()

# It is the most common form of inheritance & is the powerful tool in Python that allows you to create new classes based on existing classes.
# It allows you to reuse the code, extend it to fit your need & make it easies to manage complex systems.

class Cat (Animal):
    def __init__(self,name,sound):
        Animal.__init__(self,name,species = "Cat")
        self.sound = sound
    def make_sound(self):
        print(f"Cat produces the sound {self.sound}")
c = Cat("Pussy","Meowww")
c.make_sound()