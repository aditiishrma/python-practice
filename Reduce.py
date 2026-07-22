# REDUCE FUNCTION
# ~ Higher order function
# ~ A fn that applies a fn to  a sequence & returns a single value
# ~ Part of Function module in Python

from functools import reduce 
# needed to be imported

numbers = [1,2,3,4,5]
numbers = [1,2,3,4,5]

def sum(x,y):
    return x + y

summ = reduce (sum,numbers)
print(summ)

      # How execution actually happened :
      # Firstly, 1+2=3 then list becomes [3,3,4,5]
      # Now, 3+3=6 list : [6,4,5]
      # 6+4 = 10..[10,5]... 10 +5 = 15 final output ; 15