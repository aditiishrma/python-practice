# DOCSTRINGS Help us to understand a function properly
# They are the string literals that appear right after the definition of a FUNCTION, MODULE, CLASS or METHOD
def cube(n):
    # print(n) , if I write this then Docstring becomes NULL , as Docstrings are written right after def or any other method
    '''Take the number n, and return its cube value'''
    print(n*n*n)
cube(5)
print(cube.__doc__)

# FUNCTION DOCSTRING WITH SINGLE PARAMETER
# QUES. A Function that calculates the square of a number & add a docstring
def square(m):
    """Take the number m and return its square"""
    return m*m #print(m*m) can also be written, but other is preferred
m=int(input("Enter the value whose square you want : "))
print(square(m))
print(square.__doc__)

# FUNCTION DOCSTRING WITH MULTIPLE PARAMETERS
# QUES. Create a function that adds two numbers & document it.
def add(a,b):
    """Take the values & return the sum of them !!"""
    return a+b #print(a+b)
a=float(input("Enter the first value : "))
b=float(input("Enter the second value : "))
print(add(a,b)) # If return a+b is used, then its necessary to use print over here with function call, otherwise the value will not be printed !!
print(add.__doc__)

# MODULE DOCSTRING - It explains the whole file
# QUES. Create a module-level docstring for a student management program
'''Student Management Program, This module stores & display student information .'''
def display():
    print("Student Info")
display()

# CLASS DOCSTRING
# Create a class for a student and write a docstring
class Student() :
    '''Represents a student.
    ATTRIBUTES :
                name (str) : Student name
                age (int) : Student age'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
student=Student("Aditi",20)
print(student.name)
print(student.age)
print(Student.__doc__)

# METHOD DOCSTRING
# QUES. Write a method inside a class & document it.
class calculator():
    def multiply(self,c,d):
        """Multiply two numbers & return their product !"""
        return c*d
c=float(input("Enter the first value : "))
d=float(input("Enter the second value : "))
obj = calculator()
print(obj.multiply(c,d))

# PEP 8 - Its a document that provides guidelines & best practices on how to write python code
# It was written in 2001 by Guido Van Rossum, Barry Warsaw, and Nick Cohglam

# Zen of Python
# its basically a poem that comes in the form of an output known as an EASTER
import this