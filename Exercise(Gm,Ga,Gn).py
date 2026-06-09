import time
t = time.strftime('%H :%M :%S')
t = int(time.strftime('%H'))

# time is taken as a user input
t=int(input("Enter the time :"))
print(t)
# if elif else conditions are followed

if(t>=0 and t<12):
    print("Good Morning!!")
elif(t>=12 and t<15):
    print("Good Afternoon!!")
elif(t>=15 and t<20):
    print("Good Evening!!")
else :
    print("Good Night!!")
