##################################################################################
################################ message passing #################################

import math

def make_from_real_imag(x, y):
    def make_from_real_imag_helper(op):
        if op == 'real_part':
            return x
        elif op == 'imag_part':
            return y
        elif op == 'magnitude':
            return math.hypot(x, y)
        elif op == 'angle':
            return math.atan(y / x)
        else:
            raise Exception("Unknown op -- make_from_real_imag" + op)
    return make_from_real_imag_helper

def real_part(z):
    return z('real_part')

def imag_part(z):
    return z('imag_part')
