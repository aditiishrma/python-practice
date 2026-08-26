# ANOTHER TYPE OF INHERITANCE IN PYTHON :
# 2. MULTIPLE INHERITANCE
       # It is a powerful feature in OOP that allows a class to inherit the properties & methods from more than one parent classes.
       # Simple mean : One single child class inheriting characteristics from multiple parent classes.

# CONCEPT OF MRO (Method Resolution Order)
      # Suppose as in Multiple inheritance we have more than one parent class & for instance each of that parent class has the same name for the method
      # then Python first checks the ChildClass whether the method is present over there or not
      # then the first parent class & so on moving further

class Employee:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"The name of the employee is {self.name}")
class Dancer :
    def __init__(self,dance):
        self.dance = dance
    def display(self):
        print(f"The dance is {self.dance}")
class DancerEmployee(Employee, Dancer):  
    # The order in which the content in this () is written is what is determined by the MRO
    # Whichever class here comes first that content will be displayed & executed by the MRO
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name
D = DancerEmployee("Kathak","Aditi")
print(D.name)
print(D.dance)
D.display()
print(DancerEmployee.mro())      # Or can be written like :
print(DancerEmployee.__mro__)

# Another Example

class Animal:
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    def show(self):
        print(f"The Animal name is {self.name} and its breed is {self.breed}")
class Pet:
    def __init__(self,danger):
        self.danger = danger
    def show(self):
        print(f"The name {self.name} its breed {self.breed} and the danger level {self.danger}")
class Dog(Pet,Animal):
    def __init__(self,name,danger,breed):
        Animal.__init__(self, breed, name)
        Pet.__init__(self, danger)
a = Dog("Tony", "German Shepherd", "High")
print(a.name)
print(a.breed)
print(a.danger)
a.show()