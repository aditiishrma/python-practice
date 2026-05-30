name=str(input("Enter the name of the student: "))

subject1=float(input("Enter the marks of Biology:"))
subject2=float(input("Enter the marks of Mathematics:"))
subject3=float(input("Enter the marks of Chemistry:"))
subject4=float(input("Enter the marks of Physics:"))
subject5=float(input("Enter the marks of English:"))
subject6=float(input("Enter the marks of Physical Education:"))

total = subject1+subject2+subject3+subject4+subject5+subject6
print("Total sum is : ",total)
marks = (total/600)*100
print("Total percentage is : ", marks)
if(marks>=90):
    print("Grade A")
elif(marks>=70):
    print("Grade B")
elif(marks>=50):
    print("Grade C")
elif(49>=marks>33):
    print("Grade D")
else :
    print("Fail!!")