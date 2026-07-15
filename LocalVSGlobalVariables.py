# LOCAL VS GLOBAL VARIABLES

# LOCAL VARIABLES - The variable which is written inside a function.
# GLOBAL VARIABLE - The variable which is written outside a function but can be used inside that function too.

x = 14 # Global Variable
print(x)  # First this value got print "14"

def hello () :
    global x # Changes the value of x globally in the whole code
    x = 52
    y = 98
    print("y is a Local Variable so it will only get execute when its written inside a particular fn , if we wrote it outside then it will cause an error. Value of y is : ",y)
    print(f"The Local Variable x is {x}")    
    print("Hello World !")

print(f"The Global Variable x is {x}")   # Secondly we again get "14"
hello()                                  # Thirdly this fn is returned which prints "The local variable & Hello world" ... line
print(f"The Global Variable x is {x}")   # Lastly we'll get this 

              # Local variable gets destroyed while Global variables don't
              
# print(y)             # If we write a variable y inside the fn but print it outside the fn then we'll get an ereo