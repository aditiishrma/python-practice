# ANOTHER TYPE OF INHERITANCE IN PYTHON : 
# 5. HIERARCHIAL INHERITANCE 
           # A type of inheritance i which multiple subclasses inherit from a single parent class.
           # "One Parent Class" has "Multiple Child Classes".

class Company :
    def __init__(self,name,post,location):
        self.name = name
        self.post = post
        self.location = location
    def display(self):
        print(f"Name : {self.name} & Post : {self.post} & Location : {self.location}")

class Employee (Company):
    def __init__(self,name,id):
        Company.__init__(self,name,post = "Employee",location="Noida")
        self.id = id
    def display(self):
        Company.display(self)
        print(f"ID : {self.id}")

class Workers(Company):
    def __init__(self,name,work):
        Company.__init__(self,name,post = "Workers",location = "Noida")
        self.work = work
    def display(self):
        Company.display(self)
        print(f"Work Done : {self.work}")

w = Workers("Ramu","Sweeper")
w.display()

e = Employee("Raj","HR")
e.display()

c = Company("Accenture","High Grade","Mumbai")
c.display()

print(Company.__mro__)

# ANOTHER EXAMPLE

class Animal :
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def display(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def display(self):
        Animal.display(self)
        print(f"Breed : {self.breed}")

class Cat(Animal):
    def __init__(self,name,color):
        Animal.__init__(self,name,species="Cat")
        self.color = color

    def display(self):
        Animal.display(self)
        print(f"Color : {self.color}")

d = Dog("Tommy","Lebra")
d.display()

c = Cat("Ralia","White")
c.display()

a = Animal("Anoe","Sapiya")
a.display()