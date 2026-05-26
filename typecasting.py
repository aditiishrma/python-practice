# #TYPECASTING means changing one datatype into another datatype
a="Wahaj"
b="Aditi"
print(a+b)
a="900"
b="Aditi"
print(a+b)
a=4
b=6
print(a+b)

# #For instance suppose we don't want to change the type like we want to write the integer as a
# #  string in double quotes and don't want to chng it so there is another method for dealing up with this problem

a="9"
b="10"
print(int(a)+int(b)) # now it will give sum

a="9.9"
b="10.19"
print(float(a)*float(b))

#EXPLICIT TYPECASTING
string="109"
number=100
string_number = int(string)
sum= number+ string_number
print("The sum of numbers are :",sum)

#IMPLICIT TYPECASTING
c="99"
d="10.6"
print(int(c)+float(d)) #or simpy write c and d as an integer