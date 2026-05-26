# Python provides a set of bulit in functions that we can use to alter & modify the string
# VARIOUS STRING METHODS/BUILT=IN FUNCTIONS ARE AS FOLLOWS 

# upper()-converts whole string into UPPERCASE 
a="Aditi shArma"
print(a.upper())

# lower()-converts whole string into LOWERCASE
text="ADITI LOVES"
print(text.lower())
print(a.lower())

# rstrip()-used for removing unwanted characters from the right side
text1="!%Aditi ji%%"
print(text1.rstrip("%"))

# replace()-replaces all occurence of the string with another string
z="Sharma Ji"
print(z.replace("Sharma","Aditi"))

# split()-breaks the string & convert it into list
r="Aditi Suraj Damon"
print(r.split())

# capitalize()-turns first letter of the string into uppercase and rest into lowercase
k="intRoduction tO PYThon"
print(k.capitalize())

# center-aligns the string into center
l="introducing you all to the worldwide Python course"
print(l.capitalize())
print(l.center(100))

# count()-it tells which character is occuring how many times
print(l.count("r"))

# endswith()-it checks whether the string ends with a particular value or not
print(r.endswith("mon"))
print(r.endswith("aj",3,10))

# find()-searches for first occurence of the given value and returns its index number at which it is located,if value is absent then -1
wattpad="""Damon Salvatore is a hot guy
He is damn good looking that girls can't resist themselves from seeing
HIM"""
print(wattpad.find("I"))

# index()-similar to find()
print(wattpad.index("good"))

# isalnum()-returns true if the string contains any alpha-numeric value or else returns false
c="Rohan is 10 yrs old"
print(c.isalnum()) #returns false even if tb bar is used
d="Rohanis10yrsold"
print(d.isalnum()) #returns true over here

# isalpha()-returns true iff the string contains alphabetic values o else returns false
e="RadhEKIShoridayakro"
f="RADHE kishori2 daya kro00"
print(e.isalpha())
print(f.isalpha())

# islower()-checks whether all values of string are in lowercase or not
# isupper()--checks whether all values of string are in uppercase or not
x="ADITI"
y="aditi"
print(x.isupper())
print(y.islower())

# isprintable()-returns true if value is printable else faslse
w="aditi!\n"
print(w.isprintable())

# isspace()-returns true if string contains wide spaces  else false
q="                ADITI  SHAR  MA   "
print(q.isspace()) #returns false becoz less space is thr
v="                           r                              "
print(v.isspace())  

# istitle()-returns true if first letter of each word is capitalize else false
s="Aditi Is A Good Girl"
print(s.istitle())

# title()- capitalize each letter of the word within a string
e="python IS such a Mysterious LANGUAGE"
print(e.title())

# swapcase()-changes character casing of the string(upper to lower,lower to upper)
g="aDITI Sharma"
print(g.swapcase())

# startswith()-checks if the strings starts with a  particular value
o="Aditi Sharma"
print(o.startswith("Ad"))