#EMULATION OF DO-WHILE LOOP IN PYTHON
i=0
while True:
    print(i)
    i=i+1
    if(i%10==0): #it says when the value of i%10 becomes zero, stop the loop
        break

#ANOTHER EXAMPLE
while True:
    num=int(input("Enter the number :"))
    print(num)
    if not num>0: #It means when number becomes zero it stops the loop..
        break
# if here instead of "not num>0" , i write "num>0", then when number becomes any other value instead of 0, it stops the loop