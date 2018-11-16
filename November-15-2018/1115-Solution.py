# Uncomment below to test runtime
# import time
# start = time.time()
# Take inputs from email sample test case
ls = [10, 15, 3, 7]
k = 17
# Default Dict should be O(1) Lookups
from collections import defaultdict as dd

# We see from the problem that it only wants to see if exactly two numbers add up to k. 
# Presumably, this means we should return Yes/No instead of the two numbers.
# To solve in one pass we look for each element's compliment meaning the other number to add up to k. 
# Make a boolean defaultdict to see if we have already visited the iteration element in prev iteration.
# If we have, close out the function and return 'Yes'.
# If we have not, set the default dict at the current element's compliment to True.
# If we never see a True, return 'No'. This should execute in 1 pass as DefaultDict lookup is O(1)
# Python Documentation for Dictionary lookup time complexity: https://wiki.python.org/moin/TimeComplexity

def solver(ls, k):
    # This defaultdict will be used to see if we have already visited a list element's compliment
    closer = dd(bool)
    
    for i in ls:
        
        # We check the defaultdict for compliment first in case k is even and i == k/2
        if closer[i]: return 'Yes'
        
        # Using try/except here in case i is not a number. Test case does not tell us explicitly
        try: closer[k - i] = True
        
        # If none of the list items are numbers, this returns no in 1 pass.
        # If we did an "all" search, it would not execute in 1 pass
        except Exception: continue
    
    return 'No'

print(solver(ls, k))
# Uncomment below and at line 2 and 3 to test run time
# print("--- %s seconds ---" % (time.time() - start))
