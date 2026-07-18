# FILE HANDLING
# DIFFERENT MODES OF FILE HANDLING IN PYTHON ARE :

# write(w) mode : This opens the file for writing & creates the file if file does not exists.

f = open('AditiSharma.txt','w')    # Already present file
print(f.write("Hello Girl ! How're you ?"))   # It changes the content of 'AditiSharma.txt' file, 25 as an o/p is just the no. of characters
f.close()

my_name = open("HelloBabe.txt","w")      # Absent file
print(my_name.write("Naitik is a poor guy ! "))   # Now automatically a new file as "HelloBabe.txt" is ceated & this text also got written in it !
my_name.close()