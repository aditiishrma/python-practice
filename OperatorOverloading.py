# OPERATOR OVERLOADING IN PYTHON

# What is an Operator?
#       - An Operator is a symbol that performs some operations.(sub,add,multiply,div etc.)
print(90+12)    # Directly getting the o/p

# But Python also allows us to use operators with our own classes and objects.
# That's where operator overloading comes in.

# Operator overloading means giving a special meaning to an operator when we use it with our own objects.
class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    # Applying Dunder methods
    def __str__(self):
        # When someone tries to print, then show the no.s in this format :
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x):
        # It tells Python that when '+'  operator is used b/w 2 vector objects you should simply add them up(9+1)i...
       return Vector(self.i+x.i , self.j+x.j , self.k+x.k)

v1 = Vector(9,8,2)
print(v1)

v2 = Vector(7,6,3)
print(v2)

print(v1+v2)
print(type(v1+v2))