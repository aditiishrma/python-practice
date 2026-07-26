# "is" keyword compares the exact location of object in memory
# "==" operator compares the value.

# Eg of List
a = [9,10,11]
b = [9,10,11]
print(a is b)      # checks the exact location of object in memory
print(a==b)        # compares the value

# Eg of string and int together
integer = 12
string = "12"
print(integer is string)
print(string is integer)
print(string == integer)
                    # All return "False" because string and integer have a separate memory location when they are created.

# Eg of string and string together & int and int together - Always returns True
x = "Aditi"
y = "Aditi"
print(x is y)
print(x == y)

p = 2
q = 2
print(p is q)
print(p == q)

z = None
w = None
print(z is w)
print(z is None)
print(z == w)

num1 = 1.3
num2 = 1.2
print(num1 is num2)
print(num1 == num2)