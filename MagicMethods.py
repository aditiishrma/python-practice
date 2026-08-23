# MAGIC METHODS / DUNDERS
# These are the special methods which are defined in a class & are used to give a powerful way to manipulate objects & their behaviours.

# 1. __len__ Method
# It is used to get the length of an object.

class Employee :
    name = "aditi"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    
e = Employee()
print(e.name)
print(len(e))

# 2. __init__ Method
# A method that is automatically invoked when you create a new instance of a class.

class Name :
    def __init__(self,name):
        self.name = name

N = Name("Aditi")
print(N.name)

# 3. __str__ & __repr__ Method
# These methods are used to convert an object to a string representation.

# __str__ Method
# Used when you want to print out an object.

class HelloTune:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i

    def __str__(self):
        return f"The name of the Employee is {self.name}"
    
# __repr__ Method
# Used when you want to get a string representation of an object that can be used to recreate the object.

class HelloTune:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i

    def __str__(self):
        return f"The name of the Employee is {self.name}"
    # If we didn't comment out this section then we'll not be getting the output for __repr__ method.

    def __repr__(self):
        return f"The new name of the Employee is {self.name}"

# 4. __call__ Method
# It is used to make an object callable i.e you can pass it as a parameter to a function that will be executed when the fn is c/d.

    def __call__(self):
        print("Hey! Nice to meet you.")