# DICTIONARY - These are the ordered collection of key-value pairs, written inside the curly brackets {}
# Befoe Python 3.7 version , dictionaries were unordered collection of items but after its discovery they turn out to be the ordered ones.
dictionary = {'Name':"Aditi","Age":21,"Course":'Btech CSE'}
print("List of items of a dictionary are : ", dictionary)
print(dictionary['Name']) #print(dictionary["Name"],["Age"]) will not display the key Age's value
print(dictionary['Age'])

# ACCESSING ITEMS IN A DICTIONARY
# Acessing Single Values - Can be accessed using the get() method
item = {"USA":'Donald Trump',"India":'Narendra Modi','Italy':'Meloni'}
#print(items["France"]) # Gives an error
print(item.get('Germany')) # Gives None as the output
print(item)

# Acessing Multiple Values - Can be accessed using value() method
print(item.values())

# Accessing Multiple Keys - Can be accessed using key() method
print(item.keys())
for key in item.keys() :
    print(key) # Gives only the key terms

# Accessing key-value pairs - Can be accessed using items() method
print(item.items()) # Gives both key-values
for key,value in item.items() :
    print(f"The value corresponding to the key {key} is {value}")
    print("The value corresponding to the key {} is {}".format(key,value)) # Alternative methodfor replacing f-strings