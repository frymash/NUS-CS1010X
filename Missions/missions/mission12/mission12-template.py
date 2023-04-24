#
# CS1010X --- Programming Methodology
#
# Mission 12
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's name>, <11a/11b>

from generic_arith_min import *

###########################
# Rational Number Package #
###########################

# Copy and paste the install_rational_package procedure from Mission
# 11a below and complete the tasks below for this mission.

def install_rational_package():

    # Copy and paste your Mission 11a solution below here:


    ###########
    # Task 1a #
    ###########
    def repord_to_reprat(x):
        return None # Replace this

    ###########
    # Task 2a #
    ###########
    def RRmethod_to_ORmethod(method):
        return lambda ord, rat: method(repord_to_reprat(ord), rat)


    def RRmethod_to_ROmethod(method):
        return None # Replace this

    ###########
    # Task 3a #
    ###########
    # Copy your solution here

install_rational_package()

def create_rational(x,y):
    return get("make","rational")(x,y)

###########################
# Complex Number Package  #
###########################

# Copy and paste the install_complex_package procedure from Mission
# 11b below and complete the tasks below for this mission.

def install_complex_package():

    # Copy and paste your Mission 11b solution below here:


    ###########
    # Task 1b #
    ###########
    def repord_to_repcom(x):
        return None # Replace this

    ###########
    # Task 2b #
    ###########
    def CCmethod_to_OCmethod(method):
        return None # Replace this


    def CCmethod_to_COmethod(method):
        return None # Replace this

    ###########
    # Task 3b #
    ###########
    # Copy your solution here

install_complex_package()

def create_complex(x,y):
    return get("make","complex")(x,y)


#################
# Do not change #
#################

n3 = create_ordinary(3)
r3_1 = create_rational(create_ordinary(3), create_ordinary(1))
r2_7 = create_rational(create_ordinary(2), create_ordinary(7))

def gradeThis_rational_package():
    rationalA = is_equal(n3, r3_1)
    rationalB = is_equal(sub(add(n3, r2_7), r2_7), n3)
    if rationalA and rationalB:
        print("Well done! Your install_rational_package is complete!")
    else:
        print("Please check your solution for install_rational_package.")

n3 = create_ordinary(3)
c3_plus_0i = create_complex(create_ordinary(3), create_ordinary(0))
c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))

def gradeThis_complex_package():
    complexA = is_equal(n3, c3_plus_0i)
    complexB = is_equal(sub(add(n3, c2_plus_7i), c2_plus_7i), n3)
    if complexA and complexB:
        print("Well done! Your install_complex_package is complete!")
    else:
        print("Please check your solution for install_complex_package.")

gradeThis_rational_package()
gradeThis_complex_package()
