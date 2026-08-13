# In Python, variables can be defined at two levels :-
# 1. Class Level
# 2. Instance Level

# A Class variable remains same for all the objects created inside the class whether they have different names, salary etc.

class Employee :
    companyName = "Microsoft"
                 # A CLASS VARIABLE
    NoOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.amt = 20000
        Employee.NoOfEmployees += 1
    def showDetails(self):
        print(f'The name of the Employee is {self.name} and the salary given is {self.amt} and he/she is currently working in {self.companyName} plus its {Employee.NoOfEmployees} is its number.')


# An Instance Variable is the one that is different for different people, like here we have different names 
# via Aditi Harshit..etc..salary and other things, they simply can differ person to person.

emp1 = Employee("Aditi Sharma")
emp1.amt  = 20200
            # AN INSTANCE VARIABLE
emp1.showDetails()    # OR Employee.showDetails(emp) this line
                      # Employee.showDetails(emp)

emp2 = Employee("Harshit")

     # Suppose I wish to change the companyName (which is a class variable not an instance variable)
emp2.companyName = "Apple"
emp2.companyName = 'Google'
emp2.showDetails()   # Now emp2 company name will get changed

    # Now the question that arise is if "companyName" is a class variable why does it got changed only for Harshit and not for Aditi ?

    # The answer is first Instance Variable is being checked, since here for Harshit we have an Instance variable for the "companyName" as emp2.companyName = "Apple"
    # But if this instance variable is not present then we'll go for the searching of the class variable.
    # And when that class variable is found it will be used.

print(Employee.companyName)              # Will get the universal company i.e "Microsoft"