from icecream import ic

# Question 1
def get_nth_digit(k, n):
    """ accepts a 6 digit decimal number k (i.e., 100000 ≤ k ≤ 999999)
    and a single digit n (1 ≤ n ≤ 6). returns the the nth digit in k.
    
    int * int -> int
    """
    num_str = str(k)
    digit_str = num_str[::-1][n-1]
    return int(digit_str)

ic(get_nth_digit(375416, 4)) # Answer: 5
ic(get_nth_digit(987654, 1)) # Answer: 4
ic(get_nth_digit(123456, 6)) # Answer: 1
ic(get_nth_digit(100000, 3)) # Answer: 0


# Question 2
def bonus(days):
    """ Reads the billable days of an employee and
    output the bonus he/she has obtained in that quarter.
    
    0 to 32 days Zero
    33 to 40 days SGD$325 per Billable Day
    41 to 48 days SGD$550 per Billable Day
    > 48 days SGD$600 per Billable Day
    
    int -> int
    """
    if 0 <= days <= 32:
        return 0
    elif 33 <= days <= 40:
        return 325 * (days - 32)
    elif 41 <= days <= 48:
        return (550 * (days - 40)) + (325 * 8)
    else: # assumes days > 0
        return (600 * (days - 48)) + (550 * 8) + (325 *8)

ic(bonus(15)) # Answer: 0
ic(bonus(37)) # Answer: 1625
ic(bonus(50)) # Answer: 8200


# Question 3
def format_sum(int_string):
    """ reads in four integers as a string in the format
    int1+int2+int3+int4 and returns their sum.

    str -> int
    """
    # Iterative implementation
    total = 0
    for i in range(4):
        total += get_int(int_string, "+", i)
    return total

    # Recursive implementation:
    # if "+" not in int_string:
    #     return int(int_string)
    # else:
    #     return get_int(int_string, "+", 0) + format_sum(int_string[int_string.index("+")+1:])

    # Tail-recursive implementation:
    # final_index = 3
    # def loop(acc, n_index):
    #     if n_index == final_index+1:
    #         return acc
    #     else:
    #         return loop(acc + get_int(int_string, "+", n_index), n_index + 1)
    # return loop(0, 0)

# Predefined helper function. Do not edit.
def get_int(string, separator, n):
    return int(string.split(separator)[n])

ic(format_sum('1+2+3+4')) # Answer: 10
ic(format_sum('-10+10+-10+10')) # Answer: 0
ic(format_sum('100+10+1+0')) # Answer: 111


# Question 4
def time_difference(time1, time2):
    """ Reads the starting time and ending time as input strings,
    calculates and then displays the time difference.
    Each input strings consists of three integers, denoting the hour
    minute and second, separated by colons, e.g. "12:59:59". 
    The first string is the start time while the second is the end time. 
    
    You can assume that:

    1. Both starting time and ending time are in 24-hour format.
    2. The starting time and ending time are always in the same day.
    3. The ending time is always after the starting time.
    4. Print the time difference in the format as shown in the sample test cases.

    str * str -> str
    """
    time1_seconds = time_to_seconds(time1)
    time2_seconds = time_to_seconds(time2)
    time_diff = time2_seconds - time1_seconds
    return seconds_to_time(time_diff)
    
def seconds_to_time(seconds):
    hours = seconds // 3600
    seconds_remaining = seconds % 3600
    mins = seconds_remaining // 60
    seconds = seconds_remaining % 60
    return make_time_string(hours, mins, seconds)

# Predefined helper functions. Do not edit them.
def time_to_seconds(time):
    x = list(map(int, time.split(":")))
    return x[0] * 3600 + x[1]*60 + x[2]

def make_time_string(hours, mins, seconds):
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, seconds)

ic(time_difference('01:02:03', '13:12:11')) # Answer: 12:10:08
ic(time_difference('11:46:39', '22:31:17')) # Answer: 10:44:38
ic(time_difference('00:00:00', '23:59:59')) # Answer: 23:59:59
ic(time_difference('00:00:00', '00:00:01')) # Answer: 00:00:01


# Question 5
def triangle(side1, side2, side3):
    """ Accepts three positive integers as inputs,
    denoting lengths of three sides of a triangle
    and returns the triangle's type

    Not a triangle
     -> the length of any side is longer or equal to the sum of the other two sides.
    Equilateral
     -> all sides of a triangle have the same length.
    Isosceles
     -> two sides are equal in length and not equilateral.
    Scalene
     -> it is a triangle AND all sides are unequal (which also implies not isosceles and not equilateral).

    int * int * int -> string
    """
    if side1 >= side2 + side3 \
      or side2 >= side1 + side3 \
      or side3 >= side1 + side2:
        return "Not a triangle"
    elif side1 == side2 and side2 == side3 and side1 == side3:
        return "Equilateral"
    # elif side1 == side2 and side1 != side3 \
    #   or side2 == side3 and side2 != side1 \
    #   or side1 == side3 and side1 != side2:
    #     return "Isosceles"
    elif side1 != side2 and side2 != side3 and side1 != side3:
        return "Scalene"
    else:
        return "Isosceles" 


ic(triangle(100, 3, 4)) # Answer: "Not a triangle"
ic(triangle(5, 5, 5)) # Answer: "Equilateral"
ic(triangle(5, 3, 3)) # Answer: "Isosceles"
ic(triangle(4, 3, 5)) # Answer: "Scalene"