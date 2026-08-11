# If for some reason, we want to add a UTILITY METHOD to this code then 
# The reason behind adding the Utility method is that soemtimes I might need to add 2 numbers or perform any other critical mathematical caliculation within a class
# For this we can use "STATIC METHOD"

class Maths:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b


a = Maths(8)
print(a.num)
a.addtonum(5)
print(a.num)

# Static Methods are the methods that belong to the class not to the instance of a class.
# Defined using @staticmethod decorator
# They do not have access to the instance of the class(i.e self)