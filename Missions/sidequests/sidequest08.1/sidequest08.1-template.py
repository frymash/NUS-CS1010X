#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    """ Picture a right-angled triangle where velocity
    is the hypotenuse
    """
    angle_radians = radians(angle)
    x = velocity * cos(angle_radians)
    y = velocity * sin(angle_radians)
    return (x,y)
    

print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision


# b)
def calculate_total_acceleration(planets, current_x, current_y):
    total_ax, total_ay = 0,0
    for planet in planets:
        planet_x = get_x_coordinate(planet)
        planet_y = get_y_coordinate(planet)
        rx = planet_x - current_x
        ry = planet_y - current_y
        r = sqrt(rx**2 + ry **2)
        M = get_mass(planet)
        ax_planet = (G * M * rx) / r**3
        ay_planet = (G * M * ry) / r**3
        total_ax += ax_planet
        total_ay += ay_planet
    return (total_ax, total_ay)

print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)


# c)
# Do not change the return statement
def f(t, Y):
    rx, ry, vx, vy = Y
    ax, ay = calculate_total_acceleration(planets, rx, ry)
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(78, 27.5)


##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)

