
# This doesn't work because the canvas won't show

# frame_gen() would only work if it's
# assigned to a variable and the next function is used on it.
# e.g. (this can only work if frame_gen() and helix are
# shifted to the global scope)
# >>> test = frame_gen()
# >>> next(test) # generates next frame
# >>> next(test) # generates next frame
# >>> next(test) # generates next frame
# ...and so on


from runes import *
from math import sin, cos, pi
from time import sleep

def loading_sign(r=circle_bb,n=12, start_angle=-pi/2, delay=0.3):
    """ Returns a function that rotates a helix by 2*pi/n
    degrees every 0.2 seconds so as to simulate a loading sign

    Parameters:
    r: the image that will be replicated throughout the helix
    n: the number of times r will be replicated throughout the helix
    start_angle: the angle at which the 1st rune in the helix --
                 the darkest rune -- will be positioned in the helix
                 relative to the right half of the canvas' centre line
    delay: the time between every frame in the loading sign
           animation

    All parameters are optional.
    """
    angle = (2*pi) / n # angle between runes
    
    def helix(r,n,start_angle):
        """ Returns a helix function that produces a helix with
        n copies of rune r

        Parameters:
        r,n, start_angle: refer to loading sign's docstring
        """
        rune = scale(2/n, r)
        radius = 1/2 - 1/n

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

    def frame_gen():
        """ Rotates the initial helix continually to animate a loading sign.
        frame_gen will be called every time the program needs to generate
        a new frame in the loading sign animation.

        This rotation should loop infinitely.

        Parameters: none
        """
        curr_angle = start_angle
        while True:
            yield show(helix(r,n,curr_angle))
            curr_angle += angle
            clear_all()
            sleep(2)


    # test = trial()
    # next(test)
    # main function body
    
    
    return frame_gen()
