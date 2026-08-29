# ANOTHER TYPE OF INHERITANCE IN PYTHON : 
# 3. MULTILEVEL INHERITANCE 
       # It is a type of inheritance in which one derived class inherits from another derived class.
       # Here, one class inherits from another class & then the another class inherits from the child class.

class Animal :
    def eat(self):
        print("Animal eats.")
class Dog(Animal):
    def bark(self):
        print("Dog barks.")
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps.")

p = Puppy()    # For the Puppy class all these characters can be inherited
p.eat()
p.weep()
p.bark()

d = Dog()    # For the Dog class only these two characters can be inherited
d.eat()
d.bark()

a = Animal()    # For the Animal class only one character can be inherited
a.eat()

class Animal :
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def display(self):
        print(f"Name : {self.name} & Species : {self.species}")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species = "Dog")
        self.breed = breed
    def display(self):
        Animal.display(self)
        print(f"Breed : {self.breed}")
class Puppy(Dog):
    def __init__(self,name,age):
        Dog.__init__(self,name,breed = "Puppy")
        self.age = age
    def display(self):
        Dog.display(self)
        print(f"Age : {self.age}")
pap = Puppy("Tofu",6)
pap.display()        # we got all the charcaters that were defined from Animal class uptil the Puppy class

Ani = Animal("Leo","Dog")    # We got according to Animal class characters
Ani.display()

Doo = Dog("Babyy","German Shepherd")        # and so on..
Doo.display()