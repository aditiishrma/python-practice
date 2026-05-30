# LEVEL 1 - TAKE YOUR NAME AS INPUT & PRINT
name=str(input("Enter your name :"))
print("Hello", name,"! " "How you're doing girl?")

# TAKE TWO NO.S FROM THE USER AND PRINT THEIR
num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))

# SUM
sum= num1+num2
print("The sum of two numbers is : ", sum)

# DIFFERENCE
if(num1>num2):
   difference = num1-num2
else :
  difference = num2-num1
print("The difference of these two numbers is : ",difference)

# PRODUCT
product = num1*num2
print("The product of these two no.s is : ", product)

# DIVISION
divide = num1/num2
print("The division of theses no.s is : ", divide)

# TAKE A USER'S AGE AND PRINT
age=int(input("Enter your age bacha : "))
print("You are",age,"years old!")

# TAKE THE NAME OF THE CITY & COUNTRY & PRINT THEM IN ONE LINE
city=str(input("Enter the name of the city : "))
state=str(input("Enter the name of the state : "))
country=str(input("Enter the name of the country : "))
print("Name of city is",city,"\nName of state is",state,"\nName of country is",country)

# LEVEL 2 - STRING PRACTICE
# Take two names & join them with a space in between
name1=str(input("Enter the first person's name : "))
name2=str(input("Enter the second person's name : "))
print(name1," ",name2)

# Take a first name & last name & print
first_name=str(input("Enter the first name : "))
second_name=str(input("Enter the last name : "))
print("Full Name : ",first_name + " " + second_name)

# Take a word & print by using string concatenation
word="Python!"
print(word + " is awesome!")

# LEVEL 3 - FUNCTIONS
# Create a fn called greet() that prints
def greet():
    print("Welcome to Python !")
greet()

# Create a fn that prints the sum of two no.s
def add(x,y):
    sum=x+y
    print(sum)
x=float(input("Enter the value of x : "))
y=float(input("Enter the value of y : "))
add(x,y)

# Create a fn that joins & prints full name
def fullname(first, last) :
    join_names=first+" "+last
    print(join_names)
first=str(input("Enter the first name : "))
last=str(input("Enter the last name : "))
fullname(first,last)

# Create a fn that prints the square of a number
def square(num) :
    square=num*num
    print(square)
num=int(input("Enter the number whose square you want : "))
square(num)