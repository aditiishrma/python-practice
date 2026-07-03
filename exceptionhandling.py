num = input("Enter the number : ")
print(f"Multiplication table of {num} is : ") # f is a must !!
for i in range(1,11):
   print(f"{int (num)} X {i} ={int(num)*i}")

# if in case for this particular program a user gives string as an input then we'll get a value error. To avoid this kind of errors we can use try ... except or simply "EXCEPTION HANDLING"
a= input("Enter the number : ")
print(f"Multiplication table of {a} is : ")
try :
  for i in range(1,11):
   print(f"{int (a)} X {i} ={int(a)*i}")
except Exception as e :
  print("Invalid input")
print("Some important topics.")
print("Program execution completed successfully !!")  # Here thr will be no error becoz try..except can handle errors carefully 

# Specific type of errors can be handled
try :
  num=int(input("Enter the number : "))
  a=[9,5]
  print(a[num])
except ValueError :
  print("Number entered is not an integer !")
except IndexError :
  print("Invalid Value")