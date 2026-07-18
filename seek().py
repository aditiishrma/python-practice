# The seek() function in Python allows you to move the cursor at a specific position within a file
# Part of the built-in io module

with open('file.txt','r') as f:
    print(type(f))
    f.seek(10)         
      # This tells Python to move the cursor at position 10 starting from index 0
    data = f.read(7)
      # This means "Starting from wherever the cursor is (here its 10) 
      # read the next 7 characters and store them in a variable "data""
    print(data)

f = open('Home.txt','r')
print(type(f))
f.seek(2)
content = f.read(30)
print(content)