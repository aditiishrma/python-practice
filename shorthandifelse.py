# We can write the if...else statements in a shorter way as displayed below
a=546
b=8901
print("A") if a>b else print(b) if a==b else print("B")
    # print A agr a greater than b hai toh vrna print krdo b ki value vrna print krdo B
c = 99
print(c) if b>a else print("0")
    # in this way, we can introduce s many variables we want.
d = 100 if c>a else 0 # can write 0 as like this instead of "0" or print("0")
print(d)

aditi=10*10
naitik=10*9
print(a) if aditi>naitik else 0 if aditi<naitik else print(aditi)

# Short way to write if... else codes
p=1000000
q=11110000
result=print("Aditi") if p<q else print("Adityaa") if p==q else print("1")
print(p)