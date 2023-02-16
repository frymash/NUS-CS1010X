#
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# (a)
# unit_line_at_y : (Number) -> Curve

# (b)
# a_line : (Unit-Interval) -> Point

# (c)
def vertical_line(point, length):
    """ Returns a vertical line of the input length beginning at point
    and is drawn towards the positive y-direction

    (Point, Number) -> Curve
    """
    # 1. Define variables for the x and y coords of point
    x_coord = x_of(point)
    y_coord = y_of(point)

    # 2. Define a curve-generating function using make_point
    def line_gen(t):
        interval_length = t * length
        return make_point(x_coord, y_coord + interval_length)

    return line_gen


##draw_connected(200, vertical_line(make_point(0.1, 0.1), 0.4))

# (d)
# vertical_line: (Point, Number) -> Curve

# (e)
# draw_connected(200, vertical_line(make_point(0.5, 0.25), 0.5))

##########
# Task 2 #
##########

# (a)
# I would create a function that checks if every point in the transformed curve
# is a mirror image of its corresponding point in the original curve.
# This function would work by taking in both curves and a number
# (number of points to be tested) as inputs and produce a Boolean.
#
# Given that the transformation is a reflection about the y-axis,
# the function will check if each point has the coordinates (-x,y)
# given that its corresponding point in the original curve is (x,y).
# If the function returns True, it means that the points in the original
# curve were reflected correctly, hence proving that the curve transformation
# works properly.


# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt), y_of(pt))

    return reflected_curve
	
##draw_connected_scaled(200, arc)
##draw_connected_scaled(200, reflect_through_y_axis(arc))
