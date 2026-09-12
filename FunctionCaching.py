# FUNCTION CACHING IN PYTHON
  # Function caching means storing the result of a function so that if in future the same input is given again,
  # then Python can reuse the stored value instead of calculating it again that decreases the runtime of that fn.

# In python, Function Caching can be achieved using the "functools.lru_cache" decorator or simply writing "from functools import lru_cache"
     # First time -  Calculate - Save results
     # Same input again - Use saved results

from functools import lru_cache
import time
@lru_cache(maxsize=None)
  # @lru_cache - stores recnt results
def new_function(n):
    time.sleep(5)
    return n*5
print(new_function(20))
print("Done for 20")
print(new_function(10))
print("Done for 10")
print(new_function(15))
print("Done for 15")
print(new_function(12))
print("Done for 12")
      # Here, for all these print functions it took 5 seconds(the time assigned by the coder) for calculating the next value.
# Now prinitng these same functions again :

print(new_function(20))
print("Done for 20")
print(new_function(10))
print("Done for 10")
print(new_function(15))
print("Done for 15")
print(new_function(12))
print("Done for 12")
        # These printing functions instantly got printed, the reason being these values were already stored in the program.
        # New value
print(new_function(22))
print("Done for 22")

# KEY POINT: Don't think that when you terminate the program completely & later when you'll use it, 
# it will run with the same pace, ofc not, it will eventuallly take time as guide by the coder.

# WHEN TO USE IT AND WHEN NOT TO USE IT?
# Useful when:
   # You have limited & repeating values in the same program
# Useless when:
   # You know that the program hardly has any repeating value(thr's no need to maintain the cache, why to waste the memory)
   
# USEFUL PRACTICALLY COZ :
# Suppose a program repeatedly performs an expensive calculation:
   # Database Query
   # API request
   # Large Calculation
   # Recursive Calculation
    # Classic Eg : Fibonacci (becoz same values are calculated repeatedly)

# @cache - new modern option (unlimited cache)
from functools import cache
@cache
def square(n):
    return n*n