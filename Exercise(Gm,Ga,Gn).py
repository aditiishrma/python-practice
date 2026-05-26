import time
current_time= int(time.strftime("%H"))
current_time=int(input("Enter the time: "))
if current_time >=5 and current_time < 12:
    print("Good Morning Husband")
elif current_time >=12  and current_time < 5:
    print("Good Afternoon Wifey")
elif current_time >=5  and current_time < 10 :
    print("Good Evening Kids")
else :
    print("Good Night , lets have fun now!")