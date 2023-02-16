#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============


def staircase(levels, pic=quarter_turn_left(rcross_bb), padding=blank_bb):
    def layer(layer_num):
        padding_amount = (levels - layer_num) / levels
        return quarter_turn_left(stack_frac(padding_amount,
                                            padding,
                                            stackn(layer_num, quarter_turn_right(pic))))
    
    def remaining_steps(current_level, max_level, levels_remaining):
        if levels_remaining == 0:
            return layer(max_level)
        else:
            return stack_frac(1/levels_remaining,
                              layer(current_level),
                              remaining_steps(current_level + 1,
                                              max_level,
                                              levels_remaining - 1))
    
    return stack_frac(1/levels, layer(1), remaining_steps(2, levels, levels - 1))

    

# Staircase sample
# Level 3
"""
>>> l1 = quarter_turn_left(stack_frac(2/3, black_bb, stackn(1, quarter_turn_right(rcross_bb))))
>>> l2 = quarter_turn_left(stack_frac(1/3, black_bb, stackn(2, quarter_turn_right(rcross_bb))))
>>> l3 = quarter_turn_left(stackn(3, quarter_turn_right(rcross_bb)))
>>> clear_all()
>>> show(stack_frac(1/3, l1, stack_frac(1/2, l2, l3)))
"""

def mario(staircase_height=4, bkgrnd=blank_bb):

    jumping_mario = image_to_painter("mariojump2.png")
    luigi = image_to_painter("luigi2.png")
    flagpole = image_to_painter("flagpole2.png")

    mario_column = stack(jumping_mario, bkgrnd)
    luigi_column = stack(bkgrnd, luigi)
    bottom_left = beside(luigi_column, mario_column)
    left_half = stack(bkgrnd, bottom_left)
    
    bottom_right = staircase(staircase_height)
    top_right = flagpole
    right_half = stack(top_right, bottom_right)

    final_frame = beside(left_half, right_half)
    return final_frame

# This took me just under 2 minutes to load.
hollusion(mario())
