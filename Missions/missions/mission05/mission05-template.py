#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *


##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    """ (Curve, Curve) -> Curve

    Translates curve2 such that its 1st point will "connect"
    with the end point of curve 1. This is done by translating curve2
    by the distance between the 1st point of curve2 and the last point
    of curve1.
    """
    curve1 = scale(0.5)(curve1)
    curve2 = scale(0.5)(curve2)
    
    curve1_last_point = curve1(1)
    curve2_first_point = curve2(0)

    def distance_bt(point1, point2):
        """ (Point, Point) -> (Integer, Integer)

        Distance between point1 and point2 with respect to point1
        """
        point1_x, point1_y = x_of(point1), y_of(point1)
        point2_x, point2_y = x_of(point2), y_of(point2)
        x_distance = point1_x - point2_x
        y_distance = point1_y - point2_y
        return (x_distance, y_distance)

    def translation(dist, curve):
        """ ((Integer, Integer), Curve) -> Curve
        
        Translates curve by dist
        """
        def x_distance(dist):
            return dist[0]

        def y_distance(dist):
            return dist[1]

        final_translation = translate(x_distance(dist), y_distance(dist))
        return final_translation(curve2)
        
    distance = distance_bt(curve1_last_point, curve2_first_point)
    new_curve2 = translation(distance, curve2)
    
    return connect_rigidly(curve1, new_curve2)


##########
# Task 2 #
##########

def show_points_gosper(level, num_points, initial_curve):
    """ (Integer, Integer, Curve) -> None
    """
    def gosper():
        """ (None) -> Curve
        """
        return repeated(gosperize, level)(initial_curve)

    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5) \
                                          (gosper())
    
    draw_points(num_points, squeezed_curve)
    

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level)) \
                                        (your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn),
                                                     translate(0.5,
                                                               sin(theta))(rotate(-theta)(curve_fn))))
    return inner_gosperize

# testing
# draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
# draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
