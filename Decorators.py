# DECORATORS - These are the powerful & veratile tools that allow you to modify the behaviour of "functions" & "methods".
# They are basically used to extend the functionality of a "function" or "method" without modifying its source code.

def greet(fx):
    def mfx(*args, **kwargs):
        # *args is a method to take arguments as a TUPLE
        # **kwargs is a method that takes arguments as  a DICTIONARY(Key, Value pairs)
        print("Welcome!")
        fx(*args, **kwargs)
        print("Thankyou!")
    return mfx

def names():
    print("Aditi,Harshit")

@greet
def hello():
    print("Hello Aditi! How're you doing?")
    names()


# If I do create a add function that takes arguments so without passing a few things to mfx 
def add(num1,num2):
    print(num1 + num2)
hello()
greet(add(5,4))

# import logging
#            # logging is a built-in Python module that lets you record events that happen while your program runs.
# def logfn(func): 
             # The Decorator
#     def decorated(*args,**kwargs):
             # Wrapper function
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args,**kwargs)
#         logging.info(f"{func.__name__}returned {result}")
#         return result
#     return decorated
# @logfn
# def my_function(a,b):
#     return a+b

import logging

logging.basicConfig(level=logging.INFO)

def logfn(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@logfn
def my_function(a, b):
    return a + b

print(my_function(5, 10))