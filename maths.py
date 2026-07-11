# def add(a,b):  # def tells Python that we are going to write a function
#     return a+b
# a = int(input("Enter"))
# b = int(input("Enter"))
# # result = add(a,b)
# print(add(a,b))

def add(a,b):
    return a+b
print(__name__)
if __name__ == "__main__" :
 print("Welcoming you to solve maths !")

def welcome() :
   print("Radhey Radhey !")

print(__name__)
if __name__ == "__main__" :
 # The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module in another script
 welcome() # If this welcome() is written outside this if.. then we would get Radhey Radhey ! as an output in maths2.py file