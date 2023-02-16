#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

# Entry 1 of 1
# ============

def scarpet(s=1, r=black_bb, cutoff=0.01):
    """ Generates a Sierpinski carpet

    Parameters:
    s: scale of the carpet (relative to the initial size of r)
    r: the rune to be replicated in the Sierpinski carpet;
       this rune should have a square shape
    cutoff: the "terminating case" for recursive calls;
            no sub-carpets smaller than this number should
            recursively produce smaller carpets
    """
    if s <= cutoff:
        return quarter_turn_right(r)
    else:
        sub_per_row = 3 
        sub = scarpet(s/sub_per_row, r, cutoff)
        centre_row = quarter_turn_left( \
                        stack_frac(1/sub_per_row, \
                        sub, \
                        stack(blank_bb, sub)))
        normal_row = quarter_turn_left( \
                        stackn(sub_per_row, sub))
        return stack_frac(1/sub_per_row, \
                          normal_row, \
                          stack(centre_row, normal_row))
        
show(scarpet())

# Alternative carpet:
# show(scarpet(r=rcross_bb, cutoff=0.02))
