# FILE HANDLING
# DIFFERENT MODES OF FILE HANDLING IN PYTHON ARE :

# read(r) mode : This opens the file for reading & throws an error if file does not exists.

f = open('AditiSharma.txt','r')   # 'r mode is default, even if you don't write it program still works properly
print(f.read())                 # If the file has been opened in read 'r' mode then you can't write in that file & vice versa
f.close()