#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *


##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line

    else:
        n_minus_1_curve = scale(1/3)(kochize(level - 1))
        second_part_left = rotate(pi/3)(n_minus_1_curve)
        second_part_right = rotate(-pi/3)(n_minus_1_curve)

        left_half = connect_ends(n_minus_1_curve, second_part_left)
        right_half = connect_ends(second_part_right, n_minus_1_curve)
        return connect_ends(left_half, right_half)

    

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(0, 4000)
#show_connected_koch(4, 4000)

##########
# Task 2 #
##########

def snowflake():
    level_5_koch = kochize(5)
    first_third = rotate(2*pi/3)(level_5_koch)
    second_third = level_5_koch
    third_third = rotate(-2*pi/3)(level_5_koch)
    first_and_second_third = connect_ends(first_third, second_third)
    full_snowflake = connect_ends(first_and_second_third, third_third)
    return full_snowflake

#draw_connected_scaled(10000, snowflake())
