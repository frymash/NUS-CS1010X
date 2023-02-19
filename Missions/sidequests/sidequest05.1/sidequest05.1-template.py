#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# When unit_circle is drawn, all its points are evenly spaced out.
# However, when alternative_unit_circle is drawn, its points are very close
# to one another when t is low. As t increases, the distance between the points
# in alternative_unit_circle begins to increase as well.
#
# This is due to the implementations of unit_circle and alternative_unit_circle.
# Given that unit_circle uses a linear equation in t to calculate
# its points, the distance between its points will always be held constant.
#
# However, alternative_unit_circle uses a quadratic equation in t to calculate
# its points. Since 0 <= t <= 1, 2*pi*t*t will produce very small values
# for small values of t. As the value of t increases, the gap between points
# will increase linearly (since alternative_unit_circle is quadratic).
# Therefore, the gap between points will be
# small when t is small and will expand as t increases.

##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(t*sin(2*pi*t), t*cos(2*pi*t))

# draw_connected_scaled(1000, spiral)

# (b)
    
def heart(t):
    def reflect_curve_about_y_axis(curve):
        def reflect_point_about_y_axis(t):
            pt = curve(t)
            x,y = x_of(pt), y_of(pt)
            return make_point(-x, y)
        return reflect_point_about_y_axis
    
    spiral_mirror = reflect_curve_about_y_axis(spiral)
    return connect_rigidly(spiral, spiral_mirror)(t)

# draw_connected_scaled(1000, heart)
