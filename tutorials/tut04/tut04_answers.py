# Tutorial 4 Answers
#
# Q1
def calc_integral(f,a,b,n):
    h = (b - a) / n
    result = f(a) + f(b)
    for k in range(1, n):
        # if k % 2 == 1:
        #     result += 4 * f(a + kh)
        # else:
        #     result += 2 * f(a + kh)
        coeff = (2 + 2 *(k % 2))
        result += coeff * f(a + kh)
    return h/3 * result

# Q2
def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n-1))

def g(k):
    op = lambda x,y: x*y
    f = lambda x: x-(x+1)**2
    return fold(op, f, k)

# Q3
def accumulate(combiner, base, term, a, next, b):
    if a > b:
        return base
    else:
        return combiner(term(a),
                        accumulate(combiner,
                                   base,
                                   term,
                                   next(a),
                                   next,
                                   b))

# Q4
def sum(term, a, next, b):
    combiner = lambda x,y: x+y
    base = 0
    return accumulate(combiner, base, term, a, next, b)

# Q5
def accumulate_iter(combiner, null_value, term, a, next, b):
    result = term(a)
    a = next(a)
    while a <= b:
        result = combiner(result, term(a))
        a = next(a)
    result = combiner(result, base)
    return result

def accumulate_iter(combiner, null_value, term, a, next, b):
    terms = ()
    while a <= b:
        terms = (term(a),) + terms
        a = next(a)
    result = base
    for t in terms:
        result = combiner(t, result)
    return result

# Q6
def make_point(x,y):
    def f(o):
        if o == 0:
            return x
        else:
            return y
    return f

def make_point(x,y):
    return lambda n: x if n == 0 else y

def x_point(p):
    return p(0)

def y_point(p):
    return p(1)

# Q7
def make_segment(p1, p2):
    def f(o):
        if o == 0:
            return p1
        else:
            return p2
    return f

def start_segment(segment):
    return segment(0)

def end_segment(segment):
    return segment(1)

# Q8a
def midpoint_segment(segment):
    s = start_segment(segment)
    t = end_segment(segment)
    x_mid = (x_point(s) + x_point(t)) / 2
    y_mid = (y_point(s) + y_point(t)) / 2
    return make_point(x_mid, y_mid)

# Q8b
def make_rect(height_segment, width_segment):
    return lambda o: width_segment if o else height_segment

def height_rect(rect):
    return rect(0)

def width_rect(rect):
    return rect(1)

from math import *

def magnitude(segment):
    s_p = start_segment(segment)
    e_p = end_segment(segment)
    delta_x = (x_point(s_p) - x_point(e_p))
    delta_y = (y_point(s_p) - y_point(e_p))
    return sqrt(delta_x**2 + delta_y**2)

def height(rect):
    return magnitude(height_rect(rect))

def width(rect):
    return magnitude(width_rect(rect))

def perimeter(rect):
    return 2 * height(rect) + 2 * width(rect)

def area(rect):
    return height(rect) * width(rect)

def make_rect(p1, p2, p3):
    return lambda o: make_segment(p1, p2) if o else make_segment(p2, p3)
