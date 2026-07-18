# SLICING - It refers to extracting some part of a string.
fruit="Pomegranate"

# Finding length of the string
fruitlen=len(fruit)
print(fruitlen)
print("Pomegranate is a ", fruitlen,"letter word.")

# Slicing
print(fruit[:4]) #or[0:4] first 4 elements
print(fruit[4:9]) #including 4 but not 9th element
print(fruit[:]) #it will give the whole length
print(fruit[1:-8]) #Negative slicing
# OR
print(fruit[:len(fruit)-5])
print(fruit[2:]) #from index 2 to last element
print(fruit[::-1]) #Reverse the order
print(fruit[::2]) #Every second element

#NEGATIVE SLICING
print(fruit[-1:-7]) #Python Interpreter does this over here like -1-len(fruit) then len(fruit)-7 = 10:4
print(fruit[-7:-1]) #4:10

nm="Harry"
print(nm[-4:-2]) #len = 5 : 4-5=1,5-2=3; 1:3
#or
print(nm[1:3])