from runes import *

def circle_fractal(central_scale=1, cutoff=0.1, step=2/5, r=circle_bb):
    """ Draws a circle fractal

    Parameters:
    central_scale: the scale of the central circle as compared to circle_bb
    cutoff: the scale of the smallest circle to be generated
    step: the scale of smaller fractals as compared to the most
          recently generated fractal
    """
    pass
    
def smaller_fractal(central_scale=1, cutoff=0.1, step=2/5, r=circle_bb):
    """Generates the smaller fractals bordering the central circle

    Parameters:
    central_scale: the scale of the central circle as compared to circle_bb 
    """
    central_circle = scale(central_scale, r)
    if central_scale <= cutoff:
        return central_circle
    else:
        tinier_fractal = smaller_fractal(central_scale * step, cutoff, step, r)
        return stack(tinier_fractal, \
                     quarter_turn_right(
                         stack_frac(1/3, \
                                    tinier_fractal,\
                                    stack(central_circle, tinier_fractal))))
            
        
