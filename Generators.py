# GENERATORS IN PYTHON
# Generators are quite different from a lsi.
   # But "WHY" to compare them?
   # Because in list values are already written in it, but "Generators" generate value on the fly.
# A Generator is a special type of function that generates values one at a time, instead of creating & storing all the values in memory at once.

# MAIN DIFFERENCE :
    # Normal Function : uses "return"
    # Generator Function : uses "yield"

def my_generator():
    for i in range(20):
        yield i  # OR in place of for..i we can write yield 1/ yield 2/ yield 3...& so on

# Cretaing a Generator
gen = my_generator()
print(next(gen))
print(next(gen))
for j in gen:
    print (j)  # Using this for loop, all values uptil the given range will execute altogether

# Ques. Why hyield instead of return?
# Compare these two programs :
 # PROGRAM 1:

def my_generator2():
    for i in range(5):
        yield i

gene = my_generator2()

print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
    # Here we get the output instantly with all these 5 values one by one but


  # PROGRAM 2
def my_generator2():
    for i in range(5):
       return 1
       return 1
    
gene = my_generator2()
print(gene)

# EXAMPLE - Suppose you want numbers from 1 to 1,00,000
# A normal approach is ofc creting a list as numbers = [1,2,3,....100000] but this will eventually consume more amount of memory but instead if we use yield then memory consumption will be low.

def numbers() :
    for i in range(100000):
        yield i
generator = numbers()
print(next(generator)) # Through this we'll only be getting 1,2,3 or it depends on how many times we write print() fn
print(next(generator))
print(next(generator))

for j in generator:   # But through this we'll be getting all values printing uptil the end of the loop
    print(j)