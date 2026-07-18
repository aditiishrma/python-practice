# Imagine having a notebook with 10 pages
# A day you decide that :
        # "You don't want anything after page 5 tear off the remaining pages."
# For this, we use truncate(). 
# It cuts off the content of a fiile from a certain position omnwards.

with open('Home.txt','a') as f:
    print(f.write("Hello Cuties!"))
    f.truncate(27)

with open('Home.txt','r') as f:
    print(f.read())