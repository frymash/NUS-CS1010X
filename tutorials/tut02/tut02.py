from math import *

def magnitude(x1, y1, x2, y2):
    def square(n):
        return n*n
    
    x_diff = x2 - x1
    y_diff = y2 - y1
    return sqrt(square(x_diff) + square(y_diff))

def area(base, height):
    return 1/2 * base * height

def area2(a, b, angle_ab):
    return 1/2 * a * b * sin(angle_ab)

def area3(x1, y1, x2, y2, x3, y3):
    def herons_formula(a, b, c):
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))
    
    a = magnitude(x1, y1, x2, y2)
    b = magnitude(x3, y3, x2, y2)
    c = magnitude(x1, y1, x3, y3)
    return herons_formula(a, b, c)

# Shoelace method to find the area of a triangle using the cross product
def area4(x1, y1, x2, y2, x3, y3):
    return 1/2 * abs((x3 - x1)*(y2-y1) - (y3 - y1)*(x2 - x1))

def sum_even_factorials(n):
    result = 0
    factorial_i = 1
    for i in range(n+1):
        if i == 0:
            result += 1
            continue
        factorial_i *= i
        if i % 2 == 0:
            result += factorial_i
    return result
