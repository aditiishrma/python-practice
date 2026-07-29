# A "CLASS" is a blueprint or template of an object in Python.

class Person :              # A CLASS
    name = "Aditi"
    age = 21
    occupation = "Software developer"
# We can use the self attribute for defining 
     # The self parameter basically means the object for which the method is called.

    def info(self):
        print(f"{self.name} has an age of {self.age} and is a very hardworking person in {self.occupation} field")
# print(Person.name)
# print(Person.occupation)

# An "OBJECT" is the instance of a class.

object1 = Person()                # AN OBJECT

             # We can create as many objects using the self parameter and can call them separately.
object2 = Person()
object3 = Person()
object4 = Person()
             # ..... and so on...
object1.info()
# Changing the name and occupations 

object1.name = "Harshit"
object1.occupation = "Lawyer"
# print(a.name)
# print(a.occupation)
object1.info()

object2.name = "Raheem"
object2.age = 18
object2.info()

object3.occupation = "Actor"
object3.name = "Arpita"
object3.info()

# In same way we can create for object4 and so on....