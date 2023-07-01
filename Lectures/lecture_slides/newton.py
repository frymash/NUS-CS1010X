def sum(term, a, next, b):
  if (a>b):
    return 0
  else:
    return term(a) + sum(term, next(a), next, b)

def integral(f,a,b,dx):
  def add_dx(x):
    return x+dx
  return dx * sum(f,
                  a + dx / 2,
                  add_dx,
                  b)

def cube(x):
    return x*x*x
integral(cube,0,1,0.01)
# exact value is 1/4

dx = 0.00001

def deriv(g):
  return lambda x: (g(x+dx)-g(x))/dx

from math import sin, pi
cos = deriv(sin)


def newtons_method(g, first_guess):
  dg = deriv(g)
  def improve(x):
    return x-g(x)/dg(x)
  def is_close_enough(v):
    tolerance = 0.0001
    return abs(v)<tolerance
  def attempt(guess):
    if is_close_enough(g(guess)):
      return guess
    else:
      return attempt(improve(guess))
  return attempt(first_guess)

square = lambda x: x*x

def sqrt(a):
  return newtons_method(lambda x: square(x)-a,
         a/2)


