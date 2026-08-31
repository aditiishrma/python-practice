# A module is basically a file/library containing already written Python functionality that we can use in our program

# TIME MODULE
# The time module in Python provides a set of fns to work with time related ops such as timekeeping , formatting, & time conversion.

# time.time()
    # ~ It returns the current time as the number of seconds since January 1, 1970 (UTC) k/n as the "Epoch Time" or "Unix Timestamp"
import time

def usingWhile():
    i = 0
    while i < 00000:
        i = i+1
        print(i)

def usingFor() :
    for i in range(00000):
        print(i)


init = time.time()
usingFor()
t1 = time.time() - init

init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

start = time.time()

for i in range(000000):
    pass

end = time.time()

print("Time taken:", end - start)
print(start)
print(end)

# time.sleep()
          # ~ Used to pause the program for a particular second/s.

import time
print("Hello")
time.sleep(7) # waits for 7 seconds
print("Babyy!!")

# time.localtime()
          # It returns the current local date and time.

import time
print(time.localtime())

# time.gmtime()
          # This gives the current time in UTC
    # time.localtime() - local time
    # time.gmtime() - UTC time

# time.ctime()
          # It converts the current timestamp into a more readable form.

import time
print(time.ctime())

# time.sleep() vs time.time()
# time.sleep() - controls the flow of your program.
time.sleep(3)
# time.time() - Gives u a timestamp.
time.time()

# time.strftime()
          # It is used to format date & time in a human readable form.

import time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)

# time.strptime()
          # It is the opposite of strftime()

import time
date = "31-08-2026"
t = time.strptime(date,"%d-%m-%Y")
print(t)