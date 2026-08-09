# ACCESS SPECIFIERS / ACCESS MODIFIERS
# In Python Programming, these modifiers are used to limit the access of class methods or class variables outisde of a class while implementing the concepts of inheritance.

# VARIOUS TYPES OF IT ARE :
# 1. Public Access Specifiers 
# 2. Private Access Specifiers 
# 3. Protected Access Specifiers 

# PUBLIC ACCESS SPECIFIERS
# All variables & methods are set to public by default.
# Any instance variable followed by a "self" parameter (i.e self.var_name) is said to be a Public Specifier.

class Monuments :
    def __init__(self,name,place):
        self.name = name        # Public Attribute
        self.place = place      # Public Attribute
    def showdetails(self):
        print(f"{self.name} is located in {self.place}.")
M = Monuments("Taj Mahal", "Agra")
M.showdetails()

# PRIVATE ACCESS SPECIFIER
# These are those members of the class that can be accessed inside the class not outside it. Also k/n as the "Weak Internal Use Indicator".
# For Eg- Suppose you had parked your car with a board that says "NOT TO TOUCH" for the car but still people can touch it so its like this only.

class Student :
    def __init__(self,age):
        # self.name = name      # Public Access Specifier
        self.__age = "20"      # Private Access Modifier
    # def displaydetails(self):
    #     print(f"{self.name} is {self.__age} years old.")     # through this emthod these variables can be accessed because its inside the class not outside it
S = Student ("20")
# S.displaydetails()
# print(S.__age)              # This kinda method will throw an error because the variables are written outside the class.

# To resolve this :-
print(S._Student__age)            # This will get print, means they can be accessed indierctly.
                  # This method is known as "name mangling"

# NAME MANGLING

class MyClass:

    def __init__(self):
        self._private_attribute = "Hey I am a Private attribute"
        self.__mangled_attribute = "Hey I am mangled"


my_object = MyClass()

print(my_object._private_attribute)
print(my_object._MyClass__mangled_attribute)

# PROTECTED ACCESS SPECIFIER
# In Python, the term "protected" is used to describe a member(a method or a attribute) of a class that is indented to be accessed only by the class itself & its attributes.
class student:
    def __init__(self):
        self._name = "Aditi"
    def _funcName(self):
        return "Aditi Sharma"

class Subject(student):
    pass

obj = student()
obj1 = Subject()
print(dir(obj))
print(type(dir))     # built-in function or method

# Calling by object of student class
print(obj._name)
print(obj._funcName())

# Calling by object of Subject Class
print(obj1._name)
print(obj1._funcName)