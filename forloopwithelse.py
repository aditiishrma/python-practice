# for loop with else
for i in range(6):
    print(i)
    if i == 4: # for loop with else alongwith if & break
         break
else :
    print("STOPPPP!!!!")

# for with else can be used without using if also as :
for a in range(12):
    print(a)
else :
    print("Loop ended successfully !") # it will print all values uptil 11 & then it will print this statement

# while loop with else
i=0
while i < 10 :
    print(i)
    i = i+1 # condition for while loop, if condition is not given then only the assigned value of i will execute as 0,0,0,....0 & so on
else : 
    print("Loop ended here ! ")

# while with else alongwith if statement
i=2             # here, the loop started with 5 & satisfying the condition assigned to it goes uptil the end 
while i < 20 :
    print(i)
    i=i+2
    if i == 14:
        break
else :
    print("Ruk jaaoooo")