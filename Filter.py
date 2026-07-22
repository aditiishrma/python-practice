# Filter as we know in our home is used to clean the dirty water, it basically extracts all the dirt 
# from the dirty water and provides us with clean & safe drinking water.

# As simple as that, "filter" function filters a sequence of elements based on a given predicate(a function that 
# returns a boolean vale(True/False)) & returns a new sequence that meet the predicate.

l = [12,3,14,98,76]
def filter_function(a):
    return a>4         # List or groups all values gretare than 4

newl=list(filter(filter_function,l))
print(newl)