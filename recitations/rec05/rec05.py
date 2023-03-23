# Question 2

def contains(target, tup):
    # print(f"target: {target} | tup: {tup}")
    for element in tup:
        # print(f"id(element): {id(element)} | element: {element}")
        # print(f"id(target): {id(target)} | target: {target}")
        if element is target:
            return True
    return False

def deep_contains(target, tup):
    for element in tup:
        if element is target:
            return True
        elif type(element) == tuple:
            if deep_contains(target, element):
                return True
    return False

x = (1,2)
a = ((1,2),(3,4))
b = (x, (3,4))
# print(contains(x,a)) # False
# print(contains(x,b)) # True

x = (1,2)

# For Py 3.7: it appears that the (1,2) in the tuple c will be automatically assigned
# to the same reference as x once x appears in c.
# However, if we replace x in c by some other value, the (1,2) in c will now have a
# different reference compared to c.
# Probably a space-saving feature.
c = ((1,2), ((3,4), x), (5,6))
c_ids = [id(elt) for elt in c]
# print(id(x))
# print(c_ids)
# print(contains(x,c)) # False; works in Python 3.6 but doesn't work in 3.7.2
# print(deep_contains(x,c)) # True


# Question 3(a)
def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

def fold_right(fn, initial, seq):
    return accumulate(fn, initial, seq)

def fold_left(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(fold_left(fn, initial, seq[:-1]), seq[-1])

def pair(a,b):
    return (a,b)

def divide(a,b):
    return a/b

print(fold_right(divide, 1, (1,2,3)))
print(fold_left(divide, 1, (1,2,3)))
print(fold_right(pair, (), (1,2,3)))
print(fold_left(pair, (), (1,2,3)))
