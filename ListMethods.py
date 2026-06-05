# list.sort()
# Used for sorting or arranging elements of a list in ascending order

l=[89,23,41,56,9.9] #Float or Int both are acceptable
l.sort()
print("Sorted List is : ",l)

names=["Aditi","Alice","Zara", 'Elena','Jai']
names.sort()
print("Sorted list is :",names)

# reverse = True is used for sorting the list in descending order
l.sort(reverse = True)     # By Default reverse = False, if we don't mention it
print("Descending order of the list is : ",l)
names.sort(reverse = True)
print("Descending order of the list is : ",names)

# list.reverse()
# Used for reversing the order of the list
num=[1267,83,44,56]
num.reverse()
print(num)
colors=["Violet","Green","Orange",'Red']
colors.reverse()
print(colors)

# list.index()
# Returns the index of the first occurence of the list items
k=[1,2,3,18,1,1,4,9,0]
print(k.index(2))

# list.count()
# Tells the number of occurence of a item in the list
print(k.count(1))

# list.copy()
# Returns copy of the list
monuments=["Taj Mahal",'Victoria Memorial','Agra Fort']
newList=monuments.copy()
print(monuments)
print(newList)

numerical_values=[1,3,2,6,4]
m=numerical_values.copy()
# m[0]=90
print(numerical_values)

# list.append()
# It is used to add an item to the end of the list
r=[90,99,23,13,6]
r.append(14)
print(r)

#list.insert()
# It inserts the item at a given index
students=['Aditi',"Raj","Bhumika",'Veer']
students.insert(3,"Neeraj") # Index 3 par insert kardo Neeraj
print("List of students are : ",students)

# list.extend()
# This method adds an entire list or any other collection datatype(set,tuple,dictionary) to an existing list
a=[12,33,41,67]
b=(23,45,99) # In the form of a tuple
a.extend(b)
print("Merging a list and a tuple, we get : ",a)

# CONCATENATING TWO LISTS
c=["Aditi","Amitabh","Varun",'Kriti']
d=["Amit","Adi","Alisha"]
e=c+d # Or simply print(c+d)
print(e)