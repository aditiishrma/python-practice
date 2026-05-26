# BREAK STATEMENT- exits the loop

for i in range(12):
    print(i)
    if(i==2):
        break
    else:
        print("Mississsppi")
print("Thanks a latte")

for i in range(12):
    if(i==10):
        break
    print("5*",i+1,"=",5*(i+1))
    # if(i==10): #this can be written here as well, it will print uptil 11 here and on top it prints uptil 10
    #     break
print("Loop ko chorh kar bhaag gaya!")

# CONTINUE STATEMENT-exits the iteration

for i in range(12):
    if(i==5):
        print("Skip the iteration")
        continue #here it skips for 6,executes normally uptil 5,skips 6,then again continue
    print("5*",i+1,"=",5*i)

for i in[2,3,4,5,6,8,0]:
    if(i%2!=0):
        print(i)