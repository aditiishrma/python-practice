# SET in Python are more likely to work in the same way as those sets that are present in Mathematics.
# JOINING SETS
# union() set - It combines two sets & displays the com mon values only once.
set1={12,12,98.09,34,56}
set2={12,87,34,56,69}
print(set1.union(set2))

# update() set - It is used for adding the uncommon values from a particular set to another set.
set1.update(set2)
print(set1,set2) # Here, set1 gets update & the uncommon values from set2 are included in set1 and a new set is created

cities1 = {'Tokyo','Madrid',"Berlin","Delhi"}
cities2 = {'Tokyo',"Seoul",'Kabul',"Madrid"}
cities3=cities1.union(cities2)
print("List of new cities is : ", cities3)

cities2.update(cities1)
print(cities2,cities1)

# intersection() method - It is used to print only the common values from both the sets.
songs1 = {"Aari-Aari","Jag Ghoomeya",'Kaabil','Shararat'}
songs2 = {'Malang','Shararat',"Gehra Hua"}
songs3 = songs1.intersection(songs2)
print("Updated list of songs : ",songs3)

# intersection_update() - This method updates into existing set from another set.
songs2.intersection_update(songs1)
print("Updated list of songs : ",songs2)

# symmetric_difference() method - It prints item that are not similar to both the sets & retrun a new set
movies1={"Dhurandhar","Dhurandhar2","PremRatanDhanPayo"," ","BadrinathKi dulhania","Raabta","My Fault"}
movies2={"Dhurandhar","Sultan","PremRatanDhanPayo"," ","Humpty Sharma Ki dulhania","Raabta","Your Fault"}
print(movies2.symmetric_difference(movies1))

# symmetric_difference_update() method - It prints item that are not similar to both the sets & updates into the existing set from another set.
movies1.symmetric_difference_update(movies2)
print(movies1)

# SET METHODS
# They are the in-built methods that are used for the manipulation of the set

# isdisjoint() - This method checks whether two sets are disjoint or not, it returns "false" if the sets have common terms else "true"
# DISJOINT means two sets having nothing in common !!
colors1={"Red",'Orange',"Gray","Blue"}
colors2={"Purple",'White',"Black","Cherry Red","White","Blue"}
print(colors2.isdisjoint(colors1))

# issuperset() - This method checks if all items of a particular set are present in the original set.
print(colors2.issuperset(colors1)) # False
colors3={"Red",'Orange',"Gray","Blue"}
print(colors3.issuperset(colors1)) # True
colors4={"Red",'Orange',"Gray","Blue",'Black',"Cherry Red"}
print(colors4.issuperset(colors2)) # False
print(colors2.issuperset(colors4)) # False

cities3 = {'Tokyo','Madrid',"Berlin","Delhi"}
cities4 = {"Seoul",'Kabul'}
print(cities3.issuperset(cities4)) # False
cities5={"Seoul",'Madrid',"Kabul"}
print(cities3.issuperset(cities5)) # False
cities6 = {'Tokyo','Madrid',"Berlin"}
print(cities3.issuperset(cities6)) # True

# issubset() - This method checks if all items of the original set are present in  the particular set.
print(cities6.issubset(cities3)) # Reverse is not true i.e cities3.issubset(cities6)

# add() - It is used for adding a single item to the set.
dramas={"Jaan Nisar","Tere Bin","Shaidai","Humraahi","Sher"}
dramas.add("Fitoor")
print("List of Pakistani Dramas that I had watched : ", dramas)

# update()
dramas2={"Chand Tara","Laxmi Nivaas"}
dramas.update(dramas2)
print(dramas)

# remove() / discard() - It is used to remove an item from the list.
dramas.remove("Jaan Nisar")
print(dramas)
dramas.discard("Tere Bin")
print(dramas)
# dramas.remove("Deewangi") # remove() gives an error if that item is absent in the list
# print(dramas)
dramas.discard("Deewangi") # discard() will not give an error in that case
print(dramas)

# pop() - It is also used for removing an item from the list, but it picks any random item, that item is not defined in the code.
dramas.pop()
print(dramas) # any random elemnent gets deleted

# del - Its a keyword that deletes the set entirely & gives a NameError when it runs.
# del dramas2
# print(dramas2) # Will get an error on its excution

# clear() method - It is used to remove all the elements or items from a given set, not the whole set. Best thing is that , unlike del it does not give any error on its execution.
dramas.clear()
print(dramas) # will get set() as an output

# CHECKING IF AN ITEM IS PRESENT IN THE SET OR NOT
items={"Radhey",89,097.65,"aditi",True}
if "aditi" in items :
    print("Aditi is present") # Result
else :
    print("Absent")
if "Danish" in items :
    print("Danish is present")
else :
    print("Danish is Absent") # Result