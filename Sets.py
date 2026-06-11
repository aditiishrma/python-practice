sett={1,11,21,11,21,"Aditi","Aditi"} # This is a set
print(sett)
print(type(sett))

# tuple=(12,11,16,17,19,19,19,"Aditi","Aditi") # A Tuple
# print(tuple)

# list=["Aditi","Tashi",12,13,11,12,13] # A List
# print(list)

data_items={"Aditi","Ram","Ram","Aditi",16,90,98,98,98,98,90}
        # In a Set, they are unordered because of which any repeating value can be displayed at any index where it is present
print("The List of Data Items is as follows : ",data_items)
        # Here, in output is displayed as - {16, 98, 90, 'Ram', 'Aditi'}, unordered, no guarantee of order, order can be changed if run again, again changed as  {16, 98, 'Aditi', 'Ram', 90}
print(type(data_items))
set1={"aditi"}
print(type(set1))

# QUES> Create an empty set. Check using the type() function whether the type of your variable is a set
set2=set()
print(type(set2))

# ACCESSING SET ITEMS USING A FOR LOOP
for value in data_items :
      print(value)
for item in sett :
      print(item)