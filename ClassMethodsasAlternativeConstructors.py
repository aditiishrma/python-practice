# In OOP, the term "constructor" refers to a special type of method that is automstically executed
# when an object is created from a class.

class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

 # Additional Constructors

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

 # Normal way of creating an object       
e1 = Employee ("Aditi",25000)
print(e1.name)           # This is the basic main method for printing the name and salary of the Employee
print(e1.salary)

             # Now, suppose these name and salary (data) come in the form of a string

string = "Harshit-30000"
             # then this alternative constructor will be used.
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)