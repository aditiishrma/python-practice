# WALRUS OPERATOR IN PYTHON

# Walrus Operator was introduced since Python 3.8 version.
# Official name : "Assigned Expression Operator"
# The main purpose of it is to 
            # "Assign a value to a variable & use that value in the same expression."
# In other programming languages, we can do this simply by assigning a value to a variable but in Python we usually face this problem 
# so "Walrus Operator" was introduced as a solution to it.

# Walrus Operator can be used in a variety of concepts including the "while loops" & "if statments"

# USING "while" LOOPS

# Basic Program
a = True
#print(a=False) # This will ofc through an error
     # Correction without using walrus for it
a = False
print(a)   # 3 Lines of code

     # Using Walrus
b = True     # We can even cmnt it out, one line of code, improves readability
print(b:=False)

# Normal Program
name = str(input("Enter your name : "))
while(name != "quit"):
    print(f"Hello {name}")
    name = str(input("Enter your name : "))

# Using Walrus Operator
while(name := str(input("Enter your name : "))) != "quit":
    print(f"Hello {name}")

numbers = [1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())

# Walrus Operator assigns values to variables as part of a larger expression.

# A code without "Walrus Operator"
foods = list()
while True :
    food = input("What would you like to eat? : ")
    if food == "quit":
        break
    foods.append(food)

# A code with "Walrus Operator"
places = list()
while (place := input("Where would you like to travel? : ")) != "quit":
    places.append(place)

# USING "if" STATEMENTS

# Basic Program
names = input("Enter your name: ")
if names == "Aditi":
    print("Welcome Aditi!")

# Using Walrus
if (namee := input("Enter your name: ")) == "Aditi":
    print("Welcome Aditi!")