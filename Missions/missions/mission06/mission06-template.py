#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

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


# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(100)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

# print(profile_fn(lambda: gosper_curve(1000)(0.1), 20))

#  Time measurements:
#  1. 267.78632400009883
#  2. 276.9934960001592
#  3. 237.07107400014138
#  4. 239.54016599964234
#  5. 268.1223409999802
#
#  Average: 257.9026802000044


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# print(profile_fn(lambda: gosper_curve_with_angle(1000, lambda lvl: pi/4)(0.1), 20))

#  Time measurements:
#  1: 217.06394600005297
#  2: 197.0500309998897
#  3: 207.7982000000702
#  4: 203.07249000006777
#  5: 218.44124900007955
#
#  Average: 208.68518320003204

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# print(profile_fn(lambda: your_gosper_curve_with_angle(1000, lambda lvl: pi/4)(0.1), 20))

#  Time measurements:
#  1: 377199.50090499996
#  2: 395548.501205
#  3: 398246.5321179999
#  4: 415697.64254200005
#  5: 378936.2038029999
#
#  Average: 393125.6761146


# Conclusion:
# gosper_curve runs nearly 50ms slower than gosper_curve_with_angle on average
# when both functions were called to build a level 1000 Gosper curve 20 times.
# At the first glance, this suggests that in general, functions that are more
# customizable (like gosper_curve_with_angle) will run more quickly than those
# which are more customized (like gosper_curve).
#
# However, your_gosper_with_curve_with_angle takes hundreds of thousands of
# milliseconds to build the same level 1000 Gosper curve 20 times. Even though
# it is as customizable as gosper_curve_with_angle, it is significantly slower
# than the more customised gosper_curve.
#
# This shows that whether a function is more customizable or customized isn't a key determinant
# of function speed. The implementation of the function is more crucial as a contributing factor.

##########
# Task 2 #
##########

#  1) Yes.


#  2) In the definition of rotate, pt stores the value of curve(t) and allows
#     for this value to be reused later in the code. Since the definition of joe_rotate
#     doesn't store the value of curve(t) (given that pt was dropped), curve(t) will be
#     called twice instead every time joe_rotate is called while the variables x and y
#     are being defined within the helper function rotated_curve.
#
#     gosper_curve works by calling gosperize level times on unit_line. This means that
#     the nth-level Gosper curve is essentially a "gosperized" (n-1)th-level Gosper curve
#     (with the 0th-level Gosper curve being unit_line).
#
#     This means that if the definition of rotate is used, gosper_curve(n) -- the function
#     call used to construct the nth Gosper curve -- would call the (n-1)th Gosper curve
#     once (through curve(t)). The (n-1)th Gosper curve would then call the (n-2)th
#     Gosper curve once and so on (until the 0th Gosper curve). This means that curve(t) would run
#     in linear time. Given that the other functions in the definition of rotate run in
#     constant time, this means that gosper_curve will also run in linear time.
#
#     However, if joe_rotate replaces rotate, there would be 2 calls to the (n-1)th Gosper
#     curve. Each call to the (n-1)th Gosper curve would then make 2 additional calls to
#     the (n-2)th Gosper curve and so on. This means the number of operations in
#     gosper_curve will grow exponentially as level increases. Therefore, gosper_curve
#     will run in exponential time.

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         < 3 >         < 4 >
#                      2         < 5 >         < 10 >
#                      3         < 7 >         < 22 >
#                      4         < 9 >         < 46 >
#                      5         < 11 >        < 94 >
#
#  Evidence of exponential growth in joe_rotate.
