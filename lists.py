# LIST IN PYTHON PROGRAMMING
# If we want to store multiple items in an entity then we make or use "Lists"
# Lists are ordered, mutable collection of data items , they store multiple items in a single variable & are enclosed within [] & separated by commas

marks= [1,2,3,4,"Aditi", True] #List can store all data types including integers, string, boolean etc...
print(marks)
print(type(marks))
print(marks[0]) # Index 0 i.e 1
print(marks[3])
# print(marks[4]) # Will give an error because indexing starts from 0 so no value is present at index 4-if there is not an value at index 4
print(marks[4])
print("Naitik Gadha , suar kahin ka ek vaahiyat ladka hai !!", marks[5])

home_tour=["Hall", 1, "Room 1", 2,3,4,"Study room","Dining room","Fun Zone"]
print("My Grandma stays in ", home_tour[2])
print(home_tour[0]) # LIST INDEX means the place at which a value is stored in a list
# First Value = index[0], Second value = index[1] and so on...

# Accessing List Items or we can simple call it as "POSITIVE INDEXING"
colors = ["Red", 'Blue', "Orange"]
print(type(colors))
print(colors[0]) #Displays Red
print(colors[1]) # Displays Blue
print(colors[2]) # Displays Orange

# NEGATIVE INDEXING
# Means accessing elements simply as we do in positive indexing, but here the elements will be accessed from last position as
print(colors[-2]) # Displays second last element
print(colors[-3]) # Displays third last element

# We can convert these negative vaues as positive using len or length
print(colors[len(colors)-3]) # Positive Indexing 
print(colors[3-3])           # Positive Indexing 
print(colors[0])             # Positive Indexing 

# Check whether an item is present in the list or not
if "Orange" in colors : # in Keyword is used for this checking !
    print("Orange is present.")
else :
    print("Orange is absent.")
if "Pomegranate" in colors :
    print("Pomegranate is present . ")
else :
    print("Pomegranate is absent. ")

if 2 in marks :
    print("Present")
else :
    print("Absent")
# if we write 2 as a string over here as "2" then we'll get Absent as the output becoz 2 is present as an integer not as a string in marks list
if "pm" in "Blue" :
    print("YES ! ") 
else :
     print("NO!") # if we dont give this else condition so whether the if statement is true or false the program will always execute true only so else condition is required
    
# RANGE OF INDEX
animals = ['Dog', 'Cat', 'Lion', "Elephant", "Tiger", 'Giraffe',"Cheetah", "Rabbit","Monkey"]
print(animals[2:5:2]) #jumindex is 2 that means it jumps 2 values
print(animals[1:-1])
print(animals[-8:-4])
print(animals[:]) # it takes (animals[0:len[animals])

# Printing alternate values over here
print(animals[0:9:2])
print(animals[::2])
print(animals[-9:-1:2])
# Printing every third consecutive value
print(animals[1:9:3])

# LIST COMPREHENSION
list = [i*i for i in range(10)] # means total 10 values will come
print(list)
list = [i*i for i in range(10) if i%2 ==0]
print(list)

# Accepts item with small letter "t" in the new list
people= ["Aditi","Raj","Sarthak","Damon",'Elena']
peopleWith_t=[item for item in people if "t" in item]
print(peopleWith_t)

# Accepts item which have more than 4 letters
people= ["Aditi","Raj","Sarthak","Damon",'Elena']
peopleWith_t=[item for item in people if (len(item)>4)]
print(peopleWith_t)