#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(r,n):
    # a row here includes the image's corners
    rune_row = quarter_turn_left(stackn(n, quarter_turn_right(r)))
    
    # a column here excludes the image's corners
    rune_column = quarter_turn_right(stackn(n-2, r))
    center_section = quarter_turn_left(stack_frac(1/n, rune_column, 
                                       stack_frac(1 - (1/(n-1)),
                                                  quarter_turn_right(r),
                                                  rune_column)))
    
    return stack_frac(1/n, rune_row,
                      stack_frac(1 - (1/(n-1)), center_section, rune_row))

# Test
# show(egyptian(make_cross(rcross_bb), 5))
