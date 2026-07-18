# The tell() function is used in Python to tell the current position of the cursor in the file.
# Also a part of the built-in io module

with open('Home.txt','r')as f: 
      # selected a file where cursor is at the 0th position

    print(f.tell())
     # tell() answers the question that where exactly is the cursor pointing

    data = f.read(7)
     # It reads 7 characters then printed its value
    print(data)

    print(f.tell())
    # It tells after reading 7 characters what is the current position of the cursor.

# Other more perfect way
with open('myfile.txt','r') as f :
    dataa = f.read(3)
    print(dataa)

    current_position = f.tell()
    print(current_position)

    f.seek(current_position)

    print(f.read())