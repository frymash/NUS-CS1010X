# The 1st version of f references its formal parameters x and z.
# It also uses the value of y from the global scope as y is not
# defined in the local scope.

# x = 2
# y = 5

# def f(x,z):
# 	a = x + 1
# 	x = 7
# 	z = y + 1
# 	print("z", z)
# 	return a

# print("f(", y, ",", x, ") = ", f(y,x))


# The 2nd version of f defines y locally, hence it will not reference the
# global definition of y. However, since y is referenced before a value
# is assigned to it, an unbound local error wil be thrown.

# You could see it this way: once there is a local assignment statement for y
# within f, y is declared to exist locally in f and thus f will use the local
# definition of y. However, given that there aren't any values assigned to y
# before z = y + 1 runs, an unbound local error is rightly thrown.

# x = 2
# y = 5

# def f(x,z):
# 	a = x + 1
# 	x = 7
# 	z = y + 1
# 	y = 8
# 	print("z", z)
# 	return a

# print("f(", y, ",", x, ") = ", f(y,x))


# The 3rd version of f provides a workaround to the unbound local error.
# In this version, the global keyword is used to point any local references
# of y to the variable y in the global scope.
# Any reassignments of values to y in f will mutate the value of y in the
# global scope as well.

x = 2
y = 5

def f(x,z):
	global y
	a = x + 1
	x = 7
	z = y + 1
	y = 8
	print("z", z)
	return a

print(f"y before f is called: {y}")
print("f(", y, ",", x, ") = ", f(y,x))
print(f"y after f is called: {y}")
