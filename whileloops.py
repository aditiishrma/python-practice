# IT WAS INCREMENTING LOOP

i=1 #inititalize the value of a particular integer as 1
while(i<9): #makes a condition that i must be less than 9
    print(i)
    i=i+2 #after 2nd this 4th will be checked, it checks whether after
          #adding 2 to a no.it satisfies the conditon that i is less than 9, if yes executes it , if no stop the loop
    
while(i<=20):
    i=int(input("Enter the no. :"))
    print(i)
    i=i+222


print("Loop ended successfully!")

# NOW DECREMENTING LOOP
i=6 #given value of i
while(i>=0): #i value is greater than equal to zero
    print(i) #prints value after checking the condition
    i=i-1 #starts from 6,check 6-1=5,greater than 0,executes;5-1=4,executes & so on.....
    # if i=i+1 is written, then it becomes an infinte loop

a=5
while(a>0):
    print(a)
    a=a-1

print("Value turns out to be zero")

# DO_WHILE LOOP
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break