# Conditional Statements are basically used for checking out the conditions whether it is true or false
# Conditional Operators are listed below
# ==,>=,<=,!=,<,>

# IF-ELSE STATEMENTS
# age=int(input("Enter your age:  "))

# print(age>18)
# print(age>=18)
# print(age<18)
# print(age<=18)
# print(age!=18)

# Taking input over here
# print("Your age is:",age)
# if(age>=18):
#     print("You can drive")
# else:
#     print("You cannot drive")

# Not taking input over here
# appleprice= 300
# budget= 250
# if(appleprice<=budget):
#     print("You can buy the apples")
# else:
#     print("You cannot afford it.")

# IF STATEMENT
# a=int(input("Enter the number:"))
# if(a>0):
#     print("Number is positive") #There is  no else statment sp if you write any negative no. overe here like-99 it will not give anything

# IF-ELIF-ELSE STATEMENT
# num=int(input("Enter the number:"))
# if(num== 0):
#     print("Number equals zero")
# elif (num>0 ):
#     print("Number is positive")
# elif (num==999):
#     print("Special case")
# else:
#     print("Negative number")

#NESTED IF ELif ELSE
num=int(input("Enter the number:"))
if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num<=10):
        print("Number is in between 1 to 10")
    elif(num>10 and num<=20):
        print("Number is in between 10 to 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")