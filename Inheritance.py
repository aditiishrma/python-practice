# INHERITANCE IN PYTHON
# When a sub class (the child class) is derived from another parent class, 
# the child class is said to occupy the methods & properties of the parent class.
# This is known as "Inheritance".

# Parent Class 
class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def displaydetails(self):
        print(f"The name of the School : {self.name}\nThe location of {self.name} institute is : {self.location}")

# Child Class
class Teachers(School) :
    def education(self):
        print("The institute is a well known institute for students. It provides discipline and encourages the studengts.")


# Object Creation
school = School("St. Francis Convent School","Ghatiya Azam Khan")
school.displaydetails()

school = Teachers("Delhi Public School","Sikandra")
school.displaydetails()
school.education()

# Creating Inheritance for a family as they inherit the traits from their ancestors.
class GrandFather():
    def __init__(self,name):
        self.name = name
        print(f"Hey! I am the Grandfather & my name is {self.name}")

class Father(GrandFather):
    def __init__(self,Name):
        self.Name = Name
        print(f"I'm the Father & my name is {self.Name}")

class Child(Father):
    def __init__(self,NAME):
        self.NAME = NAME
        print(f"Myself {self.NAME} And I'm the kid of the family")

# Object creation
G = GrandFather("Ravi")
F = Father("Ram")
C = Child("Rishab")

# Inheritance means one class can use the properties & methods of another class.
# Think of it as :
          # ~ Parent Class : gives its features 
          # ~ Child Class : recieves those features & can use its own as well.
# It allows a Child Class to inherit the properties & methods of the Parent Class.
# Used for "CODE REUSABILITY"

# Without Inheritance :
class Cat :
    def eat(self):
        print("Cat eats")
class Dog :
    def eat(self):
        print("Dog eats")
c = Cat()
c.eat()
d = Dog()
d.eat()

# With Inheritance :
class Animal :
    def eat(self):
        print("Animal Eats!")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
d = Dog()
d.eat()
c = Cat()
c.eat()