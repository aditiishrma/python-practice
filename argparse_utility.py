# COMMAND LINE UTILITY
     # A command-line utility is a Python program that can be run from the terminal/command prompt, 
     # and we can give information (c/d Arguments) to the program while starting it.

# In Python, we can create our own CLU using the "argparse" which is a built-in module in Python.
# argparse module is designed to make command line programs easier & more professional.

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("num1")
# parser.add_argument("num2")
# args = parser.parse_args()
# print(float(args.num1)+float(args.num2))

import argparse
from hello import greet

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

greet(args.name)