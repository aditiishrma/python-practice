#OPERATIONS IN STRINGS

# 1. SLICING OPERATION [Extracting some part of the string]
my_values="Aditi is a good girl."
print(my_values[5:])
print(my_values[:5])
print(my_values[::-1]) #Reverses the order

# 2. INDEXING OPERATIONS [Accessing elements by position]
name="Shree Krishna" #Index starts from 0
print(name[3]) #Index 3rd element
print(name[-2]) #Last second element

# 3.CONCATENATION OPERATIONS [Joining two oe more strings together]
a="Amit Shah"
b="Indira Gandhi"
print(a+" "+b)
c="Narendra Modi"
print(a+" "+b+" "+c)

# 4. REPETITION [Printing a particular string multiple times]
print("Hii! "*100)
d="LOVE IS A WASTE OF TIME"
print(d*10)

# 5. MEMBERSHIP [Checking whether a particular word/alphabet is present in the string or not]
girl="Aditi Sharma"
print("Sh" in girl)
print(" " in girl)
print("Hr" in girl)

# 6. SPLITTING OPERATION [Breaks one particular string into parts & makes it a list]
text="Radhe Shyam Jai Kanhaiya Lal Ki"
print(text.split())

# 7. JOINING OPERATIONS[Joining elements of a string]
text1=["Radhe", "Shyam", "Jai", "Kanhaiya", "Lal", "Ki"]
result=" ".join(text1)
print(result)