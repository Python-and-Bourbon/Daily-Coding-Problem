# From problem test cases. a is first case, b is second
a, b = [1, 2, 3, 4, 5], [3, 2, 1]

# In 2 passes. First pass to multiply all nums together, second pass to divide at each index
def exclude_each_index(a):
    inclusive = 1
    for i in a: inclusive *= i
    out = [inclusive // i for i in a]
    return out

# Should be O(n*log(n)). Use the 'hoard' variable to aggregate trailing multiplication
# Still a lot of duplicated multiplication as the efficiency is only added with multiplication at
#  low indexes. May try to determine a method to eliminate redundant multiplication for O(n)
def no_division(a):
    out, hoard, prev = [], 1, 1
    while a:
        hoard *= prev
        prev = a.pop(0)
        out.append(hoard)
        for i in a:
            out[-1] *= i
    return out



print(exclude_each_index(a))
print(exclude_each_index(b))
print(no_division(a))
print(no_division(b))
