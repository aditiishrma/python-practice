# "GETTERS" & "SETTERS" help to control how variables are accessed & modified.

# GETTERS - These are the methods that are used to access the value of an object's properties.
# It is simply a method which is used to get(read) the value of an attribute.

class MyClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")
    @property
    def ten_value(self):
        return 10 * self._value

obj =MyClass(21)
print(obj.ten_value)
obj.show()

class Student:

    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age


s = Student(20)

print(s.get_age())

# SETTERS - Setter method is used to validate or this emthod is sueful to change a variable.
# This method can be added by decorating method with @property_name.setter

class Students:

    def __init__(self, age):
        self.age = age

    def set_age(self, age):
        self.age = age


s = Students(20)

s.set_age(25)

print(s.age)

class MyBuddy:
       # A class named "MyBuddy" is created
    def __init__(self,value):
        self._value = value
       # A CONSTRUCTOR

    def show (self):
        print(f"Value is {self._value}")

     # GETTERS
    @property
    def ten_value(self):
        return 10*self._value
     # SETTERS
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

# An OBJECT
obj1 = MyBuddy(10)
obj1.ten_value = 12
print(obj1.ten_value)
obj1.show()