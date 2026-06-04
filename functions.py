#  FUNCTION - A fn is a block of code that performs a particular task whenever it is called.
#  Fn is of two types - 1.BUILT-IN FUNCTIONS & 2.USER DEFINED FUNCTIONS

#  A Program that calculates GEOMETRIC MEAN(ab/a+b)
# a=24
# b=46
# gmean1=(a*b)/(a+b)
# print(gmean1)

# another Geometric mean
# c=99
# d=9
# gmean2=(c*d)/(c+d)
# print(gmean2)
# gmean3=(c*a)/(c+a)
# print(gmean3)

#here, this code of GM is of 1 line, just suppose if it is of 10 lines or even more than that then?
#Using FUNCTIONS 
def calculateGmean(a,b):
    Gmean=(a*b)/(a+b)
    print(Gmean)
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
calculateGmean(a,b)

c=int(input("Enter the value of c :"))
d=int(input("Enter the value of d :"))
if(c>d):
    print("c is the greater value")
else:
    print("d is greater or equal")
calculateGmean(c,d)

# Now for writing this thing in a shorter way we write it like-
def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is geater or equal to")

def isLesser(a,b):
    pass #It skips the current thing, and allows the intrepreter to proceed for further program
isGreater(a,b)
isGreater(c,d)

def wordPlay(x,y):
    join_names=x+" "+y
    print(join_names)
x=str(input("Enter the name of first person :"))
y=str(input("Enter the name of second person :"))
wordPlay(x,y)