# TUPLES - Tuples are ordered, immutable collection of data items that store multiple items in a single variable
tuple1=(12,23,1,1,4.5,"Aditi",'Raj')
print("The type of these values is : " ,type(tuple1),"This is the tuple : ",tuple1)

# If we write only one value in a tuple , then it becomes int,float,or string depending on the value that is present in it
tuple9=(1)
print(type(tuple9))
# so we should write it like
tup=(1,)
print(type(tup))

# As Tuples are immutable , we can't chng them, if we try thgen we'll encounter an error as
#tuple1[2]=12

# TUPLE INDEXES
countries=("Spain","Afghanistan",'India',"Pakistan",'America','Germany')
print(countries[4]) # It will display the value that is present at index 4, also referred to as the "POSITIVE INDEXING"

# NEGATIVE INDEXING
print(len(countries))
print(countries[len(countries)-2]) 
print(countries[len(countries)-4]) 
print(countries[-2]) 

# Checking for an item
values=(1,1,2,2,33,333,'Aditi',1.45)
if "Aditi" in values :
    print("Aditi is present in the tuple.")
if "Naitik" in values :
    print("Naitik is present in the tuple.")
else :
    print("Absent !")

# Range of Index
# Syntax : Tuple[start:end:jumpIndex]
tup2=(1,11,56.111,"Aditi",'Raj',True)
print("New Tuple : ",tup2[2:4])

# TUPLE METHODS - MANIPULATING TUPLES
# Tuples are immutable , hence if we want to add, remove or change tuple items then first we need to convert a tuple into a list & converting the list back into a tuple.
subjects=("Biology","Mathematics","Hindi","English","Physics","Chemistry")
temp= list(subjects)
temp.append("Social Science")
temp.pop(2)
temp[3]="General Knowledge"
subjects= tuple(temp)
print("List of all subjects as a tuple : ",subjects)

# We can directly concatenate two tuples together
food1=("Samosa","Chaat pakodi","Samosa","Samosa")
food2=("Aloo Pakodi","Bedai")
food=food1+food2
print("Merging two of the list of food items we get : ",food)