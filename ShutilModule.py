# SHUTIL MODULE IN PYTHON
       # shutil stands for "Shell Utilities"
# It is a built-in Python module that helps us to work with files & folders.

# Using Shutil, we can :
   # Copy files
   # Copy entire folders
   # Move files/folders
   # Delete folders
   # Rename files/folders indirectly by moving them

# Syntax :-
import shutil

# Various functions of the shutil module :

# shutil.copy(src,dst) - This fn copies the file located at src(source) to a new location specified by dst(destination).
#                      - If the dst file already exists then it just overwrites the file.

shutil.copy("ShutilCopy.py","ShutilCopy2.py")
    # First in terminal panel type exactly - cd "Shutil Module" then only the program will run with no errors.

# shutil.copy2(src,dst) - Similar to the previous copy fn, but it copies the metadata as well abt the original file.
shutil.copy2("ShutilCopy2.py","Metadata.py")

# shutil.copytree(src,dst) - This function copies the entire folder
shutil.copytree("My folder","My folder Backup")

# shutil.move(src,dst) - This function is used to move the file from location src to the dst file. This fn is equivalent to renaming a file in most cases.
shutil.move("Move Folder/Movefile.txt","Destination/Movefile.txt")

# shutil.rmtree(path) - This fn recursively deletes the directory or folder directly located at the path , alongwith all its content.
shutil.rmtree("Destination")
shutil.rmtree("Move folder")
