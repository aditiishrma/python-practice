#STRINGS - Anything that you enclose within single or double quotes in Python is considered a string
name = 'Aditi'
name2 = "Varsha"
print("My name is" ,name)
print("My second name is" , name2)
print("hello,",name) #or you can write it as
print("Hello," + name2)

#PRINTING He said, "I want to eat an apple"
print('He said,"I want to eat an apple".') 

#PRINTING MULTILINE STRINGS
a = '''My name is Aditi Sharma
I am currently pursuing my Bachelors of Technology.
Nice meeting you!!'''
print(a)

# OR
b = """My name is Aditi Sharma
I am currently pursuing my Bachelors of Technology.
Nice meeting you!!"""
print(b)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) gives IndexError over here which simply means that the iteration that you were doing for a particular
# string does not has the required index character over thr

#But how to do this in case of a whole long para becoz it will turn into a time consuming process then
#FOR this we use {FOR LOOP WITH STRINGS}

print("Lets use a FOR loop over here")
for character in a:
    print(character)