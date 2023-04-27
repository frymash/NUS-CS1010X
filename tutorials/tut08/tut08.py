# Question 1
def make_widget():
    stuff = ["empty", "empty", 0]
    def oplookup(msg,*args):
        if msg == "insert":
            place = stuff[2]
            stuff[place] = args[0]
            stuff[2] = (place + 1) % 2
        elif msg == "retrieve":
            return stuff[stuff[2]]
        elif msg == "stuff":
            return stuff
        else:
            raise Exception("widget doesn’t " + msg)
    return oplookup

widget = make_widget()

# (a)
# A widget object can store 2 items.
# You can interact with a widget object in 2 ways:
# 1. You can ask it to insert a new item into its storage.
#    That item will replace the oldest item in storage.
# 2. You can also ask it to retrieve the oldest item in storage. 

# (b)
widget("insert", 1)
widget("insert", 2)
widget("insert", 3)

# (c)
# 2 will always be returned as it will remain the oldest item in storage
# no matter how many retrievals you make (as long as no insertions are
# made in between retrievals).


# Question 2
def make_accumulator():
    result = 0
    def accumulate(n):
        nonlocal result
        result += n
        return result
    return accumulate

# Question 3

# (a)
def make_monitored(f):
    count = 0
    def mf(cmd):
        nonlocal count
        if cmd == "how-many-calls?":
            return count
        elif cmd == "reset-count":
            count = 0
            return
        else:
            count += 1
            return f(cmd)
    return mf

# (b)
def make_monitored_extended(f):
    count = 0
    def mf(*args):
        nonlocal count
        if len(args) == 0:
            count += 1
            return f()
        elif args[0] == "how-many-calls?":
            return count
        elif args[0] == "reset-count":
            count = 0
            return
        else:
            count += 1
            return f(*args)
    return mf

def sum_numbers(*numbers):
    s = 0
    for n in numbers:
        s = s + n
    return s

# Question 4

import random
import math

def circle(x,y):
    return math.sqrt(x*x+y*y) < 1

def make_monte_carlo_integral(pred,x1,y1,x2,y2):
    total_trials = 0
    integral = 0
    rectangle_area = abs((x2-x1)*(y2-y1))
    def oplookup(*args):
        nonlocal total_trials
        nonlocal integral
        cmd = args[0]
        if len(args) > 1:
            if cmd == "run trials" and type(args[1]) == int:
                num_trials = args[1]
                pts_in_region = 0
                total_pts = 0
                for i in range(num_trials):
                    random_x = random.uniform(x1,x2)
                    random_y = random.uniform(y1,y2)
                    random_pt = (random_x, random_y)
                    if pred(*random_pt):
                        pts_in_region += 1
                    total_pts += 1
                    total_trials += 1
                integral =(pts_in_region / total_pts)* rectangle_area
                return
        else:
            if cmd == "trials":
                return total_trials
            elif cmd == "get estimate":
                return integral
    return oplookup

"""
circle_estimate = make_monte_carlo_integral(circle, -1,-1,1,1)
circle_estimate("run trials", 1000)
print(circle_estimate("trials"))
print(circle_estimate("get estimate"))
circle_estimate("run trials", 10000)
print(circle_estimate("trials"))
print(circle_estimate("get estimate"))
"""


# Question 5

# (a)
def translate(source, destination, string):
    """ (str, str, str) -> str

    Assumes source and destination are
    strings of the same length
    """
    mappings = [(source[i], destination[i]) for i in range(len(source))]
    for mapping in mappings:
        old_letter = mapping[0]
        new_letter = mapping[1]
        target_index = string.find(old_letter)
        string = string[:target_index] + new_letter + string[target_index+1:]
    return string

print(translate("dikn", "lvei","My tutor IS kind"))

# (b)
from string import ascii_lowercase, ascii_uppercase

def caesar_cipher(n, string):
    """ (int, str) -> str
    """
    def find_new_letter(old_letter, charset):
        old_letter_index = charset.find(old_letter)
        new_letter_index = (old_letter_index + n) % alpha_len
        new_letter = charset[new_letter_index]
        return new_letter
    
    lowercase = ascii_lowercase
    uppercase = ascii_uppercase
    alpha_len = 26
    source = ""
    destination = ""
    for old_letter in string:
        if old_letter not in source:
            if old_letter in lowercase:
                new_letter = find_new_letter(old_letter, lowercase)
            else:
                new_letter = find_new_letter(old_letter, uppercase)
            source += old_letter
            destination += new_letter
    return translate(source, destination, string)

print(caesar_cipher(29, "aAbB"))
            




