"""
Question 1: Function Definitions

Below is a sequence of expressions.
What is the result printed by IDLE given the print statements?
Insert your answers into the right-side of the assignment statement
following the prints.

Assume that the sequence is to be evaluated in the order in which it is presented.

You should determine the answers to this exercise without
the help of a computer, and only later check your answers.

Observe that some of the examples shown are indented and displayed over
several lines. The indentation level of statements is significant in Python.
As Python functions don't have explicit begin or end, and no curly braces to 
mark where the function code starts and stops. The only delimiter is a
colon : and the indentation of the code itself.
"""

def square(x):
    return x ** 2
# print(square(2))
print_square_2 = 4 # An example answer
# print(square(4)) 
print_square_4 = 16 # Insert your answer here
# print(square(square(square(2))))
print_square_square_square_2 = 256  # Insert your answer here
def f(x):
    return x * x
# print(f(4))
print_f_4 = 16 # Insert your answer here
def try_f(f):
    return f(3)
# print(try_f(f))
print_try_f_f = 9 # Insert your answer here
# print(try_f(f) == try_f(square))
print_try_try = True # Insert your answer here
# print(f(3) == square(3))
print_f_3_equals_square_3 = True # Insert your answer here
# print(f == square)
print_f_equals_square = False # Insert your answer here


"""
Question 2: Odd Function

Using if-else, define a function odd(x) that returns True
when its integer argument is an odd number and False otherwise.

Hint: Consider using the '%' operator.
"""

def odd(x):
    if x % 2 != 0:
        return True
    else:
        return False


"""
Question 3: New Odd Function

Define a function new_odd(x) without if-else that returns True when its
integer argument is an odd number and False otherwise.
"""

def new_odd(x):
    return x % 2 != 0


"""
Question 4: Digit Counting

Define a function that will return the number of digits in an integer.
You can safely assume that the integers are non-negative and will not begin
with the number 0 other than the integer 0 itself.
"""

def number_of_digits(x):
    return len(str(x))


"""
Question 5: Bigger Sum

Define a function that takes three numbers as arguments and returns the
sum of the squares of the two larger numbers.

For example, given three numbers 1, 2 and 3, since 2 and 3 are larger
than 1, the bigger_sum function should return the integer value 13.

Note: You do not need to write the function is_approximately_equals.
It is pre-included on Coursemology.
"""


def bigger_sum(a, b, c):
    def sum_of_squares(x, y):
        return x ** 2 + y ** 2
        
    if a <= b and a <= c:
        return sum_of_squares(b,c)
    elif b <= a and b <= c:
        return sum_of_squares(a,c)
    else:
        return sum_of_squares(a,b)


"""
Question 6: Leap Years

Write a function is_leap_year that takes one integer parameter and decides
whether it corresponds to a leap year, i.e. is_leap_year returns True
if the input parameter is a leap year, and False otherwise.

So which years are leap years? Well, accordingly to Wikipedia:

In the Gregorian calendar, the current standard calendar in most of the
world, most years that are integer multiples of 4 are leap years.
In each leap year, the month of February has 29 days instead of 28.
Adding an extra day to the calendar every four years compensates
for the fact that a period of 365 days is shorter than a solar year
by almost 6 hours. This calendar was first used in 1582.

Some exceptions to this rule are required since the duration of a solar year
is slightly less than 365.25 days. Over a period of four centuries,
the accumulated error of adding a leap day every four years amounts 
to about three extra days. The Gregorian Calendar therefore omits 3 leap days
every 400 years, omitting February 29 in the 3 century years (integer multiples
of 100) that are not also integer multiples of 400. For example, 1600 was
a leap year, but 1700, 1800 and 1900 were not. Similarly, 2000 was a leap year,
but 2100, 2200, and 2300 will not be. By this rule, the average number of days
per year is 365 + 1/4 - 1/100 + 1/400 = 365.2425.
"""

def is_leap_year(year):
    return year % 400 == 0 or (not year % 100 == 0 and year % 4 == 0)
