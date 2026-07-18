# FILE HANDLING
# DIFFERENT MODES OF FILE HANDLING IN PYTHON ARE :

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