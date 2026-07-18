# In Python, "Lambda Function" is a small anonymous function without a name.
# They are often used in situations where a small function is required for a short duration oof time
# And are commonly used as "ARGUMENTS" to higher order functions such as map, filter, reduce etc.

# def double(x):     # This was a basic function
#     return x * 2

# Lambda fn can serve useful when we pass any function as an argument.

def appl(a,value):
    return 6 + a(value)

double = lambda x:x*2    # Using Lambda function
cubee = lambda x:x*x*x
avg = lambda x,y,z:(x+y+z)/2
print(double(5))
print(cubee(2))
print(avg(12,3,78))
print(appl(cubee,2))   # 6 + (2*2*2)

cube = lambda y :y*y*y
print(cube(9))

# c = int(input("Enter the first number : "))
# d = int(input("Enter the second number : "))
print(lambda c,d: print(f"{c}*{d}={c*d}"))