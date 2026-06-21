# Dictionary uses several built-in methods for manipulation
# FOR CHANGING ITEM OF A DICTIONARY
# update()
names={"Name1":"Aditi Sharma",'Name2':'Alisha Patel','Name3':"Radhika Jaiswal","Name4":"Veer Chauhan"}
print(names)
names.update({'Name1':'Ram'})
print(names)
names.update({"Name5":"AmarJeet Singh"})
print(names)

# FOR REMOVING ITEMS FROM DICTIONARY
# clear() - Removes all items
# names.clear() 
print(names)

# pop() - Remove the item that has been asked 
info={"name":'Aditi','age':21,'course':'Btech CSE'}
info.pop('course')
print(info)

# popitem() - It removes last key-value pair from the dictionary
info.popitem()
print(info)

# del keyword - It deletes whole of the dictionary
#del info
#print(info) # Throws an error
del names['Name4']
print(names)