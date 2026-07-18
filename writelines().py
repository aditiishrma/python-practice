# Introducing the other methods which are required or used in File Handling :

# writelines() method - It writes a sequence of strings to a file

f = open('myfile.txt','w')
lines = ["line 1\n","line 2\n","line 3"]
f.writelines(lines)
f.close()

      # readlines() & writelines() come up together at most of the places.