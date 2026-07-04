# raising Custom Errors in Python
# For some user input , the programmer wishes to give an error on its own instead of the Python Interpreter
# For this we use Custom errors

num = input("Enter any number between 5 & 20 : ")
if num == "quit":
    print("Program ended !!")
else :
    num = int(num)
    if num<5 or num>20 :
        raise ValueError("Value should lie between 5 & 20")
    else :
        print("Good Input!!")

# Raising different kind of errors 
# ValueError : The entered value is wrong but of the same datatype
age=int(input("Enter your age : "))
if age < 0 :
    raise ValueError("Age can't be negative ! ")
else :
    print("Correct Age. Congratulations !! You're growing up")

# TypeError : When the entered datatype is wrong or different than the required
name = str(input("Enter your Name : "))
if not isinstance(name,str):
    raise TypeError("Name can't be an integer value")
else :
    print("Good Name !!")

age = 20
if isinstance(age,int):
    print("YES")
else :
    print("NO")

# There are different types of errors than can be handled including
# NameError - Variable missing
# IndexError - List position missing
# KeyError - Dictionary key missing
# ZeroDivision Error - Divide by zero
# FileNotFound Error - File missing
# etc etc......