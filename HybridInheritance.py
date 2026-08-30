# ANOTHER TYPE OF INHERITANCE IN PYTHON : 
# 4. HYBRID INHERITANCE 
        # Hybrid Inheritance is simply a combination of two or more types of inheritance.
        # In Python, it can be implemented by creating a class hierarchy, in which a base class is inherited by 
        # multiple derived classes & one of the derived class is further inherited by a sub-derived class.

class Animal :
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def display(self):
        print(f"Name : {self.name} , Species = {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name , species = "Dog")
        self.breed = breed
    def display(self):
        Animal.display(self)
        print(f"Breed : {self.breed}")

class Cat(Animal):
    def __init__(self,name,color):
        Animal.__init__(self,name,species = "Cat")
        self.color = color
    def display(self):
        Animal.display(self)
        print(f"Color : {self.color}")

class Puppy(Dog):
    def __init__(self,name,breed,age):
        Dog.__init__(self,name,breed)
        self.age = age
    def display(self):
        Dog.display(self)
        print(f"Age : {self.age}")

class Pet(Puppy, Cat):
    def __init__(self,name,breed,age,color):
        Puppy.__init__(self,name,breed,age)
        # Cat.__init__(self,name,color)
                 # With the two above lines we get two different info, first for Puppy & then for Cat
        self.color = color
    def display(self):
        Puppy.display(self)
        # Cat.display(self)
        print(f"Color : {self.color}")

p = Pet("Tomy","German Shepherd",4,"White")
p.display()

Pu = Puppy("Leo","Antolio",7)
Pu.display()

c = Cat("Pussy","White-Black")
c.display()

d = Dog("Tony","Cutie")
d.display()

a = Animal("Ana","Sapience")
a.display()

# Structure for the code :
        # Pet → Puppy → Dog → Cat → Animal → object

# PRACTISE QUESTION
class Character :
    def __init__(self,name,level):
        self.name = name
        self.level = level
    def display(self):
        print(f"Character's Name : {self.name} & Level : {self.level}")

class Warrior(Character):
    def __init__(self,name,weapon):
        Character.__init__(self,name,level = "Warrior")
        self.weapon = weapon
    def display(self):
        Character.display(self)
        print(f"Weapon : {self.weapon}")

class Mage(Character):
    def __init__(self,name,spell):
        Character.__init__(self,name,level = "Mage")
        self.spell = spell
    def display(self):
        Character.display(self)
        print(f"Spell : {self.spell}")

class Knight(Warrior):
    def __init__(self,name,weapon,armor):
        Warrior.__init__(self,name,weapon = "Knight")
        self.armor = armor
    def display(self):
        Warrior.display(self)
        print(f"Armor : {self.armor}")
        
class BattleMage(Knight,Mage):
    def __init__(self,name,level,weapon,armor,spell):
        Knight.__init__(self,name,weapon,armor)
        self.spell = spell
    def display(self):
        Knight.display(self)
        print(f"Spell : {self.spell}")

b = BattleMage("Aria", 20, "Sword", "Dragon Armor", "Fireball")
b.display()

k = Knight("AllieCat","Bow","Vampire Armor")
k.display()

m = Mage("MegaPi","Spell")
m.display()

w = Warrior("Pikaso","Hammer")
w.display()

c = Character("Leader","Level Final")
c.display()

