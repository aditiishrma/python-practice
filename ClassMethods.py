# Classes are a way to define custom datatypes that can store data and define functions that can manipulate the data.

  # A "CLASS METHOD" is a method that is bound to the class not to the instance of the class.
  # It operates on the whole class not on a specific instance.

class Employee :
    company = "Apple"      # Class Variable
    def show(self):
        print(f"The name of the company is {self.company} and the name of the employee is {self.name}")

    @classmethod
    # Through this method the the first argument that comes to a method is Instance as seen below
    def changecompany(cls, newcompany):
        cls.company = newcompany

e1 = Employee()
e1.name = "Aditi"
e1.show()
e1.changecompany("Microsoft")
e1.show()

print(Employee.company)