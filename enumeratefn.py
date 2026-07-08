# Enumerate function is a built-in fn in Python that allows you to loop over a sequence & get the index & value of each element in the sequence at the same time.

    # Writing a program without using an Enumerate Function
marks = [45,90,99,81,100,33]
index = 0
for mark in marks :
    print(mark)
    if index == 4 :
        print("Well Done!")
    index +=1

    # Writing this same program using an Enumerate Function
for index,mark in enumerate(marks) :
    print(mark)
    if index == 4 :
        print("Well Done !")

cars = ["BMW",'Mercedes',"Lamborghini","Bugati",'Scorpio','Ferari']
for index,car in enumerate(cars) :
    print(index,car)

# We can even specify the starting index like instead of starting from 0 we can make it start from any other number like 1,2...& so on
for index,car in enumerate(cars,start=3) :
    print(index,car)