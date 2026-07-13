import os

# If I would be making a 100 days of code challenge then it would be using the "os module"
if(not os.path.exists("data")) :
 os.mkdir("data") # this line alongwith the import os line , simple held us a folder name "data"

for i in range(0,100) :
 os.mkdir(f"data/Day{i+1}") # this created a 100 days data in "data" where one can store different things