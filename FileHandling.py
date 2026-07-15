# FILE HANDLING
# DIFFERENT MODES OF FILE HANDLING IN PYTHON ARE :

# read(r) mode : This opens the file for reading & throws an error if file does not exists.

f = open('AditiSharma.txt','r')   # 'r mode is default, even if you don't write it program still works properly
print(f.read())                 # If the file has been opened in read 'r' mode then you can't write in that file & vice versa
f.close()

# write(w) mode : This opens the file for writing & creates the file if file does not exists.

f = open('AditiSharma.txt','w')    # Already present file
print(f.write("Hello Girl ! How're you ?"))   # It changes the content of 'AditiSharma.txt' file, 25 as an o/p is just the no. of characters
f.close()

my_name = open("HelloBabe.txt","w")      # Absent file
print(my_name.write("Naitik is a poor guy ! "))   # Now automatically a new file as "HelloBabe.txt" is ceated & this text also got written in it !
my_name.close()

# append(a) mode : It opens the file for adding an extra content at the end of the file & creates a new file if the file does not exists.

my_name = open("HelloBabe.txt","a")       # Just write "a" mode over here but use the write only instead of append to add content
print(my_name.write("Love is a waste of time."))
my_name.close()

# create(x) mode : It creates a file & gives an error if file already exists.

# f = open("HelloBabe.txt","x")      # Already existing file
f = open("Radhey.txt","x")           # Cretaes a new file named "Radhey.txt"
f.close()

# text(t) mode : It is used to handle the text file. r & rt or w & wt are same as text mode is the default mode in python.

# f = open('AditiSharma.txt','rt') 

# binary(b) mode : Used to handle the binary files.

# The 'with' statement
# Alternatively, you can use the with statement to close the file even if we don't write close() 

with open('AditiSharma.txt','a') as f :
    f.write("Heyy")