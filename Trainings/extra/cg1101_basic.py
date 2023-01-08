from icecream import ic
from math import sqrt

# Question 1
def BMI(mass, height):
    if mass <= 0 or height <= 0:
        return None
    else:
        result = mass / height ** 2
        if result <= 0:
            return None
        else:
            return result

# Question 2
def investment(P, R, N):
    return round(P*(1 - (R/100)**(N+1))/(1 - R/100), 2)


# Question 3
def ip_format(ip_address):
    """ Returns an IP address in dotted decimal format
   
    Input: IP address string in binary format
   
    string -> string
    """
    def bin_to_dec(b):
        """ Returns the decimal representation of a binary number
        Assumes that the input string is 8 letters long
        (just like a 8-bit binary number should be)
        
        string -> string
        """
        reverse_b = b[::-1]
        result = 0
        
        for i,c in enumerate(reverse_b):
           if c == "1":
               result += 2**i
               
        return str(result)
    
    
    if len(ip_address) < 8:
        return ""
        
    elif len(ip_address) == 8:
        return bin_to_dec(ip_address)
    
    else:
        return bin_to_dec(ip_address[:8]) + "." + ip_format(ip_address[8:])

# ic(ip_format('00000011100000001111111111111111'))
# ic(ip_format('11001011100001001110010110000000'))

# Question 4
def get_bigger_root(a,b,c):
    """ Reads three coefficients a, b, c representing equation ax^2 + bx + c = 0. 
    This function returns the bigger one between its two roots
    (assuming that both roots are real numbers).

    Output must be correct to 2 d.p.

    (int * int * int) -> int
    """
    root1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    root2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    ic(root1, root2)

    if root1 > root2:
        return round(root1, 2)
    else:
        return round(root2, 2)

ic(get_bigger_root(1, -8, 15))
ic(get_bigger_root(3, 11, 9))


# Question 5
def is_sum_odd(num):
    num_str = str(num)
    digit_list = list(num_str)
    digit_list = map(int, digit_list)
        
    result = sum(digit_list)
    return result % 2 != 0

ic(is_sum_odd(12))
ic(is_sum_odd(123789))
ic(is_sum_odd(1))