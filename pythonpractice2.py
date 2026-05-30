# LEVEL 4 & 5 - SMALL PROGRAMS & CHALLENGING TASKS
# Create a small program that takes marks of English, Maths, Science, then print total & avg marks

name=str(input("Enter the name of the student : "))
sub1=float(input("Enter the marks of English : "))
sub2=float(input("Enter the marks of Maths : "))
sub3=float(input("Enter the marks of Science : "))

total_marks=sub1+sub2+sub3
print("The total marks of the student is : ", total_marks)

average_marks=(total_marks)/3
print("The Average marks of the student is : ", average_marks)

# Create a program that takes length & breadth and print the area of rectangle
length=float(input("Enter the length of the rectangle : "))
breadth=float(input("Enter the breadth of the rectangle : "))

area=length*breadth
print("The area of the rectangle is : ", area)

# Create a program that takes the price of a product & a qnty, then prints the total bill
price=int(input("Enter the price of the product to be bought : "))
quantity=int(input("Enter the quantity to be bought : "))

total_bill=price*quantity
print("The total bill of gthe product is : ", total_bill)

# Create a mini marksheet program for 5 subjects & display Student Name, total marks, percentage
name=str(input("Enter the name of the student : "))

sub1=float(input("Enter the marks of English : "))
sub2=float(input("Enter the marks of Maths : "))
sub3=float(input("Enter the marks of Science : "))
sub4=float(input("Enter the marks of Computer : "))
sub5=float(input("Enter the marks of Hindi : "))

total_marks = sub1+sub2+sub3+sub4+sub5
print("The total marks of the student is : ", total_marks)

percentage = (total_marks/500)*100
print("The percentage of the student is : ", percentage)

# Create a fn calculator(a,b) that prints addition, subtraction, multiplication, division
def calculator(a,b):
    sum=a+b
    print(sum)
    
    subtraction=a-b
    print(subtraction)
    multiplication=a*b
    print(multiplication)
    if(a>b):
        division=a/b
        print(division)
    else :
       division=b/a
       print(division)

a=float(input("Enter the first value : "))
b=float(input("Enter the second value : "))
calculator(a,b)

# Create a fn that takes two names and print "Friendship between Aditi & Riya"
def friends(name1,name2):
    print("Friendship between", name1,"and",name2,"is mesmerizing!")

name1=str(input("Enter the first person's name : "))
name2=str(input("Enter the second person's name : "))
friends(name1,name2)