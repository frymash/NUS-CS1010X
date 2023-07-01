# Part 1
#
# WORKING WITH TUPLE and LIST
x = (1,2,3)
y=[x,x]
#-------
#x[1] ="b" - error as tuple can't do assignment like list can
x =(1,"b",3) # does not change y at all
print(y)
print(x.count(3))
print(x.index(3))
print(x.index("b"))
#print(x.index(2))  - error as 2 is not found in x
#--------
#y[0][0] = ("c")
w = [y, y]
y[0]=[]  # direct assignment is possible here but not for tuple
print(w)
#---------
#y = y[0].append("a")  - this is not what you wanted for y
y[0].append("a")
print(w)
# WORKING WITH LIST
s = [1,2,3,4]
s.append(5)
s.remove(3)
s.insert(1, "11")
s.insert(10, "99")
s.pop(0)
s.pop(-1)
s.pop() # without saying is popping the last one
######################

# Part 2
#
# illustration to show passing by value
def f(x):
    x = "new"
    return

a = 10
f(a)
print(a)

a = "xyz"
f(a)
print(a)

a = (10, 20)
f(a)
print(a)

# -- let do the assigment as tuple still to see how.
def g(x):
    x = (100,200)
    return

a = (10, 20) # this is actually a new tuple as compare to the previous one of the same value
g(a)
print(a)

##############################
# illustration to show passing by object reference
# do x, then y, then z one-by-one

x = ["a"]
y = ["a"]
z = ["a"]
def f(x1,y1,z1):
    x1.append(2)
    y1 = ["a", 2]
    z1 = z1.append(2)
    # if Python is call by reference (which is false), z outside will be empty too
    return

f(x,y,z)
print(x,y,z)

# Part 3
#
####################################
# recursive with different data type
#
ztuple = (1,3,5,1,3,5)
zlist = [1,3, 5, 1, 3, 5]

# O(n^2) time and space - no side effect
def product_tuple (t):  
    if t==():
        return 0
    elif len(t) == 1: # t[1:]==()
        return t[0]
    else:
        return t[0]*product_tuple(t[1:])

print(product_tuple(ztuple))

# O(n) time and space - side effect
def product_list(t):  
    if t==[]:
        return 0
    elif len(t) == 1:
        return t.pop(0)
    else:
        return t.pop(0) * product_list(t)

print(product_list(zlist)) 

# O(n^2) time and space - no side effect
def product_list_v2(t): 
    if t==[]:
        return 0
    elif len(t) == 1:
        return t[0]
    else:
        return t[0] * product_list_v2(t[1:])

zlist = [1,3, 5, 1, 3, 5]
print(product_list_v2(zlist))

# product_list without side-effect
# time and space O(n)
def product_list(t):  
    def helper(t):
        if t==[]:
            return 0
        elif len(t) == 1:
            return t.pop(0)
        else:
            return t.pop(0) * helper(t)
    temp = t.copy()
    return helper(temp)

#################
#
# abstraction - good to have if there are enough time but no time
#
def product(t):
    if len(t) == 0:
        return 0
    elif len(t) == 1:
        return t[0]
    else:
        return t[0]*product(t[1:])

print("ans:", product(zlist))  # time O(n^2) space O(n^2), no side effect

print("ans2:", product(ztuple))


