# Introducing the other methods which are required or used in File Handling :

# readlines() method - This method is used to read a single line of a code, if one wants to read multiple lines tthen should use a loop. 

f = open("AditiSharma.txt",'r')
while True :
    line = f.readline()         # if we've "f.readlines()" then we'll get the o/p as a list in one line
    if not line :
        break
    print(line)
    print(type(line))

f = open("HelloBabe.txt","r")
i = 0
while True :
    i = i+1
    line=f.readline()
    if not line :
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in maths is : {m1*2}")
    print(f"Marks of student {i} in english is : {m2*2}")
    print(f"Marks of student {i} in gk is : {m3*2}")