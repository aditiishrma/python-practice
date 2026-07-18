# FILE HANDLING
# DIFFERENT MODES OF FILE HANDLING IN PYTHON ARE :

# append(a) mode : It opens the file for adding an extra content at the end of the file & creates a new file if the file does not exists.

my_name = open("HelloBabe.txt","a")       # Just write "a" mode over here but use the write only instead of append to add content
print(my_name.write("Love is a waste of time."))
my_name.close()