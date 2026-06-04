# In Python, an ARGUMENT is a value that you pass to a fn when you call it.
def greet(name) :
    print("Hello",name)
greet("Aditi") # Here, Aditi is an argument - it refers to the actual value passed to the function

# Alternative method for printing the same thing using functions could be
# def greet() :
#     name="Aditi"
#     print("Hello" , name)
# greet()

# There are basically 4 types of arguments in Functions
# 1. DEFAULT ARGUMENTS
def average(a=10,b=9) :
    avg=(a+b)/2
    print("The average of the two numbers is : ", avg) # Alternatively, we could write in place of avg as (a+b)/2
average(1, 9) # If here i write another numbers, then it neglects the previous one & takes the average of the new numbers

def name(name1,name2 = "Aditi", name3 = "Shiva",name4="Gargi", name5="Krishna") :
    print("Hello" , name1,name2,name3,name4,name5)
name("Amy","Harshit","Aditya","Jai") #It basically replaces the previous names & insert new names in place of those old names!!
#As thr are only 4 names , so first 4 names will get replace not the last one

# 2. KEYWORD ARGUMENTS
def average (a,b=10): # If we dont give the value of a, then it will automatically consider 12,15 value & will neglect b=10 over here
    print(type(b))

    print("The average of these two numbers is : ",(a+b)/2)
# average()  # First way, old 9 and 10 value will be taken
average(12,15) # Second way, new values will be taken
#These two we've already seen for default arguments 
average(b=8,a=2) #KEYWORD ARGUMENT here, order is changed but written in key=value form

def name(lname,mname,nname):
    print("Hello", lname,mname,nname)
name(mname="Aditi",lname="Krishna",nname="Radha") # Order is written in a way that is changed but the o/p generated will be in the respective order as the argument is defined in key=value manner

# 3. REQUIRED ARGUMENTS - Mandatory arguments that are required when arguments are not defined in key=value pair
def name(name1,name2) :

    print(type(name1)) # shows class string of name1

    print("Hello", name1,name2)
name(name1="Harshit", name2="Aditi") # Error will be shown if I dont write the name2 value over here

def average(a,b,c=1,d=0):
    print("The average of four numbers is : ", (a+b+c+d)/2)
average(2,3,d=4) #it ignores d value as zero, and takes it to be 4

# 4. VARIABLE-LENGTH ARGUMENTS
# Sometimes we may need to pass more arguments than those defined in actual function, there are two ways to achieve this :
# A. ARBITRARY ARGUMENTS
# The fn accesses the arguments by passing them in the form of a "TUPLE"
def average(*numbers) :
    print(type(numbers))
    sum = 0
    for i in numbers :
        sum = sum+i
        print("The average is : ", sum/len(numbers))
average (5,6,9,10) # Multiple values can be given 

def name(*name) :
    print("Hello", name[0], name[1])
name("Aditi", "Amy", "Harshit") # Here third name will not be displayed becoz name[2] is not defined.....

# B. KEYWORD ARBITRARY ARGUMENTS
# The fn accesses the arguments by passing them in the form of a "DICTIONARY"
def name(**name):
    print("Hello," , name["name1"], name["name2"], name["name3"])
name(name1="Aditi", name2="Arpit", name3="Harshit")

# Alternatively, the Arbitrary argument code can be written in the following other manner as 
# RETURN STATEMENT
def name(name1,name2):
    return "Heya " +name1 + " " "and " + name2 + ""
print(name("Aditi", "Arpit")) 