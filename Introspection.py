# OBJECT INTROSPECTION
# Object Introspection means to know what is present in an object & how we can use it.

# For this we have 2 methods & 1 attribute as :
# METHODS : dir()             ATTRIBUTE : __dict__
#           help

# THE dir() METHOD
# This method/function returns a list of all the attributes & methods(including dunder methods) that are available for the object.

list1 = [12,67,90,0.9]
print(dir(list1))
print(list1.__class__)
print(list1.__delattr__)

class Student :
    def __init__(self,name):
        self.name = name
    # def display(self):
    #     print(f"Aditiiii")
s = Student("Aditi")
# s.display()
print(dir(s))

# THE __dict__ ATTRIBUTE
# This attribute returns a dictionary representation of an object's attributes.
# It show the data/attributes that are actually stored in an object or a class.

class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

n = Name("Aditi", 20)

print(n.__dict__)

# THE help() METHOD
# It is used to get the "help documentation" for an object including the description of its attributes and methods.

print(help(Name))