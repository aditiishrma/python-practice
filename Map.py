# Suppose we've a function that returns the cube of any number

def cube(x):
    return x*x*x

print(cube(2))
    # Here, we know the output would be "8"
    # But suppose we've a list of items as :

l = [12,87,31,8,9,6]
    # We want that the output gives the cube of all thses numbers 
    # For this, we have one choice as the "FOR LOOP"

# newl = []
# for l in list :
#     newlist.append(cube(l))

# print(newl)

    # But this way the program becomes more complex to organize.
    # Hence, here we use the "map" function.

newl = list(map(cube,l))
print(newl)  # It will return a map object, that can easily be resolved using the term "list" just before map in previous line  

# An example of map function using Lambda Function
numbers = [2,5,8,9,4]
double = list(map(lambda x : x*2, numbers))
print(double)

# LAMBDA FUNCTION
# Instead of defining the function using def ... we can simply use the lambda fn as :

items = [6,0,98,1,2,4]
newitems=set(map(lambda x : x*2, items))  # Like cube one or any other..
print(newitems)