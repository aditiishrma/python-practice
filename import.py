# There are various "Libraries" in Python that we can get into our code usin g the "import" keyword
# List of Python Libraries
# 1. Operating System Libraries (os,sys)
# 2. Mathematical Libraries (math,NumPy)
# 3. Data Analysis Libraries (Pandas)
# 4. Data Visualization Libraries (matplotlib)
# 5. Random Number Libraries (random)
# 6. Date & Time Libraries (datetime)
# 7. File & data Format Libraries (json)
# 8. Web Request Libraries (requests)
# 9. Machine Learning Libraries (scikit-learn, tensorflow, PyTorch)

# import os
# print(os.getcwd())

import math
print(dir(math))
result=math.sqrt(12)
print(result)

# from keyword
# used to import a specific function or variable from the module.
from math import modf
result = modf(12)
print(type(modf))
print(result)

from math import sqrt,pi
calculation = sqrt(64)
print(calculation)
calculation = sqrt(64) * pi
print(calculation)
print(type(sqrt))

# One can also import everything from a module using the * keyword
from pandas import *

# "as" keyword - it allows to rename imported module for convenient use
import math as m
resullt =m.sqrt(81) * m.pi
print(resullt)
print(m.pi)

# dir function - it is used to view all the functions & variables that are present in a module
import pandas
print(dir(pandas))

# import flask Needed to be installed
# import tensorflow 

# from aditi import welcome,aditi
import aditi as ad
ad.welcome()
print(ad.aditi)  # A file created by me is imported in this way