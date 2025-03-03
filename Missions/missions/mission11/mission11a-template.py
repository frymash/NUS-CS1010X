#
# CS1010X --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: A0269863J ARVIND NATARAJAN

###############
# Mission 11a #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x, x)

# (a) What are the types of the input and output of the generic square operation?
# Answer:(GenericNum, GenericNum) -> GenericNum

# (b) Why would we prefer to define square in the above way, rather than:
# def square(x):
#    return apply_generic("square", x)
# Answer: If we define square in the latter way, we would need to add
# another row to the operation table and define a separate implementation
# of square for each relevant generic number type.
# Doing so would be more time-consuming as compared to just defining square
# in the above way.

##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by the
# name of the operator and a tuple of strings. For example, the add operator is
# indexed by ’add_ord’ and (’ordinary’, ’ordinary’); negation is indexed by
# ’negate_ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by
# ’make_ord’ and just a string ’ordinary’. Explain why we have such a difference.

# Hint: Consider the differences in the process of the creation of a Generic-Num,
# such as create_ordinary, and the operations we can apply on Generic-Num, such
# as add. How is make_ord invoked, and how is add_ord invoked?

# Answer:

# The difference in indexing between a generic operator and the constructor
# arises from the differences in their invocations.
#
# Every generic operator will call apply_generic, a function which would wrap
# all the type tags of the data passed to it in a tuple.
#
# To illustrate how this works, we'll analyse the chain of function calls
# that follow an initial call to add.
#
# The chain of function calls after the initial call for add would
# be as follows:
#
# add(x, y)
# -> apply_generic("add", x, y)
# -> get("add", ("ordinary, "ordinary"))(x,y)
# (Notice the appearance of parentheses around the type tags in
# the previous line)
# -> _operation_table["add"][("ordinary", "ordinary")](x)
# -> add_ord(x,y)
# -> make_ord(x+y)
# -> tag(x+y)
# -> attach_tag("ordinary", x+y)
# -> ("ordinary", x+y)
#
# In contrast, the constructor works by taking in some input x and attaching
# an "ordinary" tag to it.
#
# The chain of function calls after the initial call to create_ordinary would
# be as follows:
#
# create_ordinary(x)
# -> get("make", "ordinary")(x)
# -> _operation_table["make"]["ordinary"](x)
# -> make_ord(x)
# -> tag(x)
# -> attach_tag("ordinary", x)
# -> ("ordinary", x)
#
# Both chains of function calls provide some clues as to why their indexings
# differ:
#
# 1. The 1st indexes ("add_ord" vs "make_ord") represent the key functions
#    that the get function needs to look up based on the initial function call.
#
#    Given some input represented as ordinary numbers, the add operator must
#    eventually call add_ord as it's the variant of the add operator for
#    ordinary numbers.
#
#    On the other hand, the constructor must eventually call make_ord
#    as it is the variant of the make function that is used to construct
#    ordinary numbers.
#
# 2. The 2nd indexes (("ordinary", "ordinary") vs "ordinary), however, differ
#    due to the fact that apply_generic is in the chain of calls
#    following add(x,y) but is NOT in the chain of calls following
#    create_ordinary(x).
#
#    apply_generic wraps all type tags of the arguments passed to it
#    within a tuple (e.g. if *args=[("ordinary", x), ("ordinary", y)],
#    apply_generic would store the type tags as ("ordinary", "ordinary"))
#    before passing this tuple as the 2nd argument to get (to be used as the
#    2nd index in the _operation_table lookup in get). 
#
#    Since apply_generic("add", x, y) is called after add(x,y), the 2nd index
#    for the add operator must be a tuple that stores the tags of 2 ordinary
#    numbers -- ("ordinary", "ordinary").
#
#    However, get("make", "ordinary")(x) is called right after create_ordinary(x).
#    Hence, there is no need for "ordinary" to be wrapped in a tuple.



##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

# first_try = create_rational(9, 10)
# second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way: second_try
# What happens: A "Bad tagged datum" exception is raised.
# Why it happens: Rational numbers must be represented by a "rational" tag and
#                 2 ordinary numbers. When the wrong way is used, the underlying
#                 numbers in the rational number (9, 10, 3, and 10) would not be
#                 represented as ordinary numbers, hence the rational number would
#                 be incorrectly formatted. Functions that operate on rational
#                 numbers would not work with rational numbers that are incorrectly
#                 formatted.

##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# r2_7 = create_rational(create_ordinary(2), create_ordinary(7))
# r3_1 = create_rational(create_ordinary(3), create_ordinary(1))

# csq = square(sub(r2_7, r3_1))


##########
# Task 5 #
##########

# Within the generic rational number package, the internal add_rat function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer:
# add should be the generic addition operator for Generic-Num, not the addition operator
# for Generic-Rat.

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x, y))
    def reprat(x, y):
        return (x, y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add, sub, mul, div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x, y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x, y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x, y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x, y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )
    
    def negate_rat(x):
        """ (RepRat) -> Generic-Rat
        """
        numer_x, denom_x = numer(x), denom(x)
        return make_rat(negate(numer_x), denom_x)

    def is_zero_rat(x):
        """ (RepRat) -> Boolean
        """
        return is_zero(numer(x))

    def is_eq_rat(x, y):
        """ (RepRat, RepRat) -> Boolean
        """
        def simplify(x):
            numer_x, denom_x = numer(x), denom(x)
            return div(numer_x, denom_x)
            # Don't use div_ord here since
            # a) div_ord is private to install_ordinary_package()
            #    and can't be accessed outside it
            # b) the generic operator for division, div, wil call div_ord
            #    after it detects that numer(x) and denom(y) are
            #    ordinary numbers.

        # print(f"x: {x}, y: {y}")
        # print(f"x: {simplify(x)}, y: {simplify(y)}")
        return simplify(x) == simplify(y)
        
    
    put("make", "rational", make_rat)
    put("add", ("rational", "rational"), add_rat)
    put("sub", ("rational", "rational"), sub_rat)
    put("mul", ("rational", "rational"), mul_rat)
    put("div", ("rational", "rational"), div_rat)
    put("negate", ("rational",), negate_rat)
    put("is_zero", ("rational",), is_zero_rat)
    put("is_equal", ("rational", "rational"), is_eq_rat)

install_rational_package()

def create_rational(x, y):
    return get("make", "rational")(x, y)

# Change the values for the test variables below
r1_2 = create_rational(create_ordinary(1), create_ordinary(2))
r2_4 = create_rational(create_ordinary(2), create_ordinary(4))
r1_8 = create_rational(create_ordinary(1), create_ordinary(8))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
