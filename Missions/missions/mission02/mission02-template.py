#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(r, n):
    if n == 1:
        return r
    else:
        return beside(r, stackn(2, fractal(r,n-1)))
     

# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(r, n):
    curr = r
    for i in range(1, n):
        prev = curr
        curr = beside(r, stackn(2, prev))
    return curr

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# show(fractal_iter(rcross_bb, 5))


###########
# Task 1c #
###########

def dual_fractal(r1, r2, n):
    if n == 1:
        return r1
    else:
        return beside(r1, stackn(2, dual_fractal(r2, r1, n-1)))


# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(r1, r2, n):
    if n % 2 == 0:
        r1, r2 = r2, r1

    curr = r1
    
    for i in range(1, n):
        prev = curr
        if i % 2 == 0:
            curr = beside(r1, stackn(2, prev))
        else:
            curr = beside(r2, stackn(2, prev))

    return curr

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 8))


# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(r1, r2, r3, r4):

    def mosaic(r1, r2, r3, r4):
        row1 = beside(r4, r1)
        row2 = beside(r3, r2)
        return stack(row1, row2)

    l1 = overlay_frac(3/4, blank_bb, r1)
    l2 = overlay_frac(1/2, blank_bb, r2)
    l3 = overlay_frac(1/4, blank_bb, r3)
    l4 = r4

    return mosaic(l1, l2, l3, l4)

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
