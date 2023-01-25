from runes import *

def scarpet(s=1, r=rcross_bb, cutoff=0.02):
    """ Generates a Sierpinski carpet of size n

    Parameters:
    s: scale of the carpet
    r: the rune to be replicated in the Sierpinski carpet;
       this rune should have a square shape
    cutoff: the "terminating case" for recursive calls;
            no subcarpets smaller than this number should
            recursively produce smaller carpets
    """
    if s <= cutoff:
        return quarter_turn_right(rcross_bb)
    else:
        sub = scarpet(s/3)
        centre_row = quarter_turn_left( \
                        stack_frac(1/3, \
                        sub, \
                        stack(blank_bb, sub)))
        normal_row = quarter_turn_left( \
                        stackn(3, sub))
        return stack_frac(1/3, normal_row, stack(centre_row, normal_row))
        
show(scarpet())
