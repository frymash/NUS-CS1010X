#############################################################
##
## First implementation of rational number with tuple
##
#############################################################
print("")
print("First Implementation of Rational Number with tuple")

# 1. constructor(s)
## return a rational number with given numerator & denominator
from math import gcd
def make_rat(n, d):
    g = gcd(n, d)
    return (n//g, d//g)

# 2. selector(s)
## return the numerator of the input rat number
def numer(rat):
    return rat[0]

## return the denominator of the input rat number
def denom(rat):
    return rat[1]

# 3. predicates
## check whether 2 rational numbers are equal in value
def equal_rat(x1, x2):
    return numer(x1)*denom(x2) == numer(x2)*denom(x1)

## check whether an input number is indeed a rational number
def is_rat(rat):
    return type(rat)==tuple and len(rat)==2 and \
           type(numer(rat))==int and type(denom(rat))== int

# 4. printers
## print out nicely the rational number
def print_rat(rat):
    print(str(numer(rat)) + '/' + str(denom(rat)))

    
# 5. operations: various arithmetic operations on rational numbers
def add_rat(x1, x2):
    n1, d1 = numer(x1), denom(x1)
    n2, d2 = numer(x2), denom(x2)
    return make_rat(n1 * d2 + n2 * d1, d1 * d2)

def sub_rat (x1, x2):
    n1, d1 = numer(x1), denom(x1)
    n2, d2 = numer(x2), denom(x2)
    return make_rat(n1 * d2 - n2 * d1, d1 * d2)

def mul_rat (x1, x2):
    return make_rat (numer(x1)*numer(x2), denom(x1)*denom(x2))

def div_rat(x1, x2):
    return make_rat (numer(x1)*denom(x2), denom(x1)*numer(x2))


one_half = make_rat(1, 2)
print("is_rat(one_half) is", is_rat(one_half))
print("one_half is")
print_rat(one_half)
one_third = make_rat(1, 3)
print("one_third is")
print_rat(one_third)
print("add_rat(one_half, one_third) is")
print_rat(add_rat(one_half, one_third))
print("mul_rat(one_half, one_third) is")
print_rat(mul_rat(one_half, one_third))
print("add_rat(one_third, one_third) is")
print_rat(add_rat(one_third, one_third))
print("div_rat(one_third, one_third) is")
print_rat(div_rat(one_third, one_half))

##############################################################
##
## Second implementation of Rational Number -- using function
##
##
## only need to amend the following 4 routines
## - make_rat
## - numer
## - denom
## - is_rat
##
print("")
print("Second Implementation of Rational Number with function")

from math import gcd
def make_rat(n, d):
    g = gcd(n, d)
    return lambda x: n//g if x else d//g

# 2. selector(s)
## return the numerator of the input rat number
def numer(rat):
    return rat(True)

## return the denominator of the input rat number
def denom(rat):
    return rat(False)

## check whether an input number is indeed a rational number
import types
def is_rat(rat):
    return isinstance(rat, types.FunctionType) and \
           type(numer(rat))==int and type(denom(rat))== int

one_half = make_rat(1, 2)
print("is_rat(one_half) is", is_rat(one_half))
print("one_half is")
print_rat(one_half)
one_third = make_rat(1, 3)
print("one_third is")
print_rat(one_third)
print("add_rat(one_half, one_third) is")
print_rat(add_rat(one_half, one_third))
print("mul_rat(one_half, one_third) is")
print_rat(mul_rat(one_half, one_third))
print("add_rat(one_third, one_third) is")
print_rat(add_rat(one_third, one_third))
print("div_rat(one_third, one_third) is")
print_rat(div_rat(one_third, one_half))
