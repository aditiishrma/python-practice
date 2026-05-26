import time
x=int(time.strftime("%H"))
x=int(input("Enter the time: "))
# x is the variable to match
match x:
    case 0:
        x >=5 and x < 12
        print("Good Morning")
    case 1:
        x >=12 and x<17
        print("Good Afternoon")
    case 2:
        x >=17 and x < 20
        print("Good Evening")
    case _:
        print("Good Night")

# This can also be written using if, elif, elif and else instead of using match statements as

import time
x=int(time.strftime("%H"))
x=int(input("Enter the time :"))
# x is the variable to match
if x>=5 and x<12:
    print("Good Morning")
elif x>=12 and x<17:
    print("Good afternoon")
elif x>=17 and x<21:
    print("Good Evening")
else :
    print("Good Night")  