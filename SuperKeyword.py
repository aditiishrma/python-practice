# THE Super KEYWORD
# Sometimes we need to call Parent class methods from Child class methods, for this we use the super keyword.
#    ~ It is used to refer to the parent class.
#    ~ It is more useful when a class inherits from the multiple parent classes & one wants to call a method from one of those parent classes.

class ParentClass:
    def parent_method(self):
        print("This is the parent method.") # Secondly we'll get this.

class ChildClass(ParentClass):
    def parent_method(self):
            print("This is Aditi.") # thirdly, this will execute
            super().parent_method()
    def child_method(self):
        print("This is the child method.")       # First this will execute
        super().parent_method()       # Secondly, it will go to parent class and run the parent method

child_object = ChildClass()
child_object.child_method()        # First call
child_object.parent_method()       # Second call

parent_object = ParentClass()
parent_object.parent_method()      # Third call

class Employee :
     def __init__(self,name,id):
          self.name = name
          self.id = id
class Programmer(Employee) :
     def __init__(self,name,id,lang):
          self.name = name
          self.id = id
          self.lang = lang

rohan = Employee("Aditi Sharma","123")
aditi = Programmer("Gargi","098","Python")
print(aditi.name)
print(aditi.id)
print(aditi.lang)