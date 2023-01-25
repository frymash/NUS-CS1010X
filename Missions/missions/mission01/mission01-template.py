#
# CS1010X --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(r1, r2, r3, r4):
    row1 = beside(r4, r1)
    row2 = beside(r3, r2)
    return stack(row1, row2)


# Test
# show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))

##########
# Task 2 #
##########

def simple_fractal(r):
    return beside(r, stack(r,r))

# Test
# show(simple_fractal(make_cross(rcross_bb)))

