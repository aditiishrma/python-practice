# Constructor is a special method in a class which is used to create and initialize an object of a class.
# The main purpose of it is to initialize or assign values to the data members of that class.

class Person :
    def __init__(self,name,occ):
        print("Hey I'm a person")
        self.name = name
        self.occ = occ
        # A "CONSTRUCTOR"

    def info(self):
            print(f"{self.name} is a {self.occ}")
    
a = Person("Aditi","Developer")     # An "OBJECT"
                 # The constructor is called whenever an object is created
b = Person("Harshit","Developer")     # Creating another "OBJECT" as well, same way it will aslo be called
        # This calling of Object
        # can be done n times...
a.info()
b.info()

# There are two types of "constructors" in Python :-

# 1. PARAMETERIZED CONSTRUCTOR
# When the Constructor accepts arguments alongwith self , like :

class Game :
     def __init__(self,model,type):        # model and type are the extra parameters alongwith self
          self.model=model
          self.type=type
     def info(self):
          print(f"{self.model} is a {self.type}")
object1 = Game("GTA-5","Latest Version")
object1.info()

# 2. DEFAULT CONSTRUCTOR
# When the constructor doesn't accept any other arguments from the object except the self parameter :

class Monument:
     def __init__(self):
          print("Monuments are the most attractive things that increase " \
          "tourism in the country")
Monument()