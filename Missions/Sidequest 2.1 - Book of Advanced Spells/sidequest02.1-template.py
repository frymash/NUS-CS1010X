#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

# Tail-recursive version (builds the tree from top to bottom):
def tree(n,r):
    def build_layer(layer,zoom,r):
        """ Builds the tree from its base upwards.
        The bottommost layer is the 1st layer while
        the topmost layer is the nth layer.

        Parameters:
        layer: the layer number
        zoom: the magnification of the rune; like a "camera zoom" figure
        r: rune image of choice
        """
        if layer == 1:
            return r
        else:
            return overlay_frac(1/layer, \
                                scale(zoom/n, r), \
                                build_layer(layer-1,zoom+1, r))
    
    return build_layer(n,1,r)


'''
# Iterative version (builds the tree from bottom to top):

def tree(n,r):
    """ Builds the tree from the top down.
    The bottommost layer is the 1st layer while
    the topmost layer is the nth layer.
    """
    curr = r
    layer_num = 1
    for i in range(n-1,0,-1):
        layer_num += 1
        prev = curr
        curr = overlay_frac(1/layer_num, scale(i/n,r), prev)
    return curr
'''

# Test
# show(tree(4, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

# Note that sin and cos measure angles in radians
# Runes should start from 270 deg (3pi/2)

def helix(r,n,start_angle=-pi/2):
    """ Returns a helix function that produces a helix with
    n copies of rune r

    Parameters:
    r: the rune to be used
    n: number of rune copies to be displayed on the canvas
    start_angle: the angle which the 1st rune will be positioned relative to
                 the positive x-axis
    """
    rune = scale(2/n, r)
    radius = 1/2 - 1/n
    angle = (2*pi) / n # angle between runes

    def posn(rune_order):
        """ Determines position of a rune on the canvas based on its number
        in the order of n runes (starting from the 1st rune at -pi/2)

        Parameters:
        rune_order: the current rune's index in the order of the runes to be drawn;
        posn determines the position of the xth rune.
        start_angle: refer to helix's docstring
        """
        return translate(radius * cos(start_angle + (angle*(rune_order-1))), \
                        -radius * sin(start_angle + (angle*(rune_order-1))), \
                        rune)

    def draw_runes(rune_order, layers_left):
        """ Draws every rune from the rune_order'th rune to n-1'th rune.

        Parameters:
        rune_order: the current rune's index in the order of the runes to be drawn
        layers_left: the remaining number of layers that need to be drawn
        """
        if layers_left == 1:
            return posn(rune_order)
        else:
            return overlay_frac(1/layers_left, \
                                posn(rune_order), \
                                draw_runes(rune_order+1, layers_left-1))
        
    return draw_runes(1, n)
    

# Test
# show(helix(make_cross(rcross_bb), 9))
