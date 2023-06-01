# Question 1

memoize_table = {}
def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name] = {}
    table = memoize_table[name]
    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args)
            table[args] = result
            return result
    return helper

def collatz_distance(n):
    result = 0
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        result += 1
    return result

def max_collatz_distance(n):
    return max(map(collatz_distance, range(1, n+1)))

"""
def max_collatz_distance(n):
    if n == 1:
        return 0
    else:
        return max(collatz_distance(n), \
                   max_collatz_distance(n-1))

def max_collatz_distance_memo1(n):
    def helper(n):
        if n == 1:
            return 0
        else:
            return max(collatz_distance(n), \
                       max_collatz_distance_memo1(n-1))
    return memoize(helper, "collatz_distance")(n)

"""

def collatz_distance_memo(n):
    def helper(n):
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + collatz_distance_memo(n//2)
        else:
            return 1 + collatz_distance_memo(3*n + 1)
    return memoize(helper, "collatz_distance")(n)

def max_collatz_distance_memo1(n):
    return max(map(collatz_distance_memo, range(1, n+1)))


# My own version which can't work for big numbers
def max_collatz_distance_memo2(n, d={0:0}):
    if n in d:
        return d[n]
    else:
        d[n] = max_collatz_distance_memo2(n-1, d)
        return max(collatz_distance(n), d[n])


# Question 2

from urllib.request import urlopen
from urllib.parse import urlsplit
from urllib.error import *


# (a) If the website does not utilise the HTTP protocol, the function
# would not be able to access it.

# (b) Errors are more natural and more easily extensible. Nested exceptions also
# grant some flexibility.
# TA's answer: The programmer will know what to fix explicitly.
# An empty string will not really tell what the programmer is going wrong.

# (c)

class InternetFail(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value) 
"""
def httpget(url):
    try:
        parsed = urlsplit(url)
        if not parsed.scheme: # protocol insertion
            url = "http://" + url
        elif parsed.scheme != "http ":
            raise ValueError("Unknown protocol")
        return urlopen(url).read()
    except HTTPError:
        raise InternetFail("Internet error")
    except URLError:
        raise ValueError("User error")
    except:
        raise
"""

# TA's answer
def httpget(url):
    parsed = urlsplit(url)
    if not parsed.scheme:
        url = "http://" + url
    elif parsed.scheme != "http://":
        raise ValueError("Unknown protocol")
    try:
        return urlopen(url).read()
    # When we catch an exception and throw it again,
    # we are rethrowing that error.
    except HTTPError as err:
        raise InternetFail("HTTP Error - " + str(err))
    except URLError as err:
        raise ValueError(str(err))
    except Exception as err:
        raise err
    

def download_URLs(URL_filenames):
    for url, filename in URL_filenames:
        try:
            with open(filename, "wb") as myFile:
                myFile.write(httpget(url))
        except (InternetFail, ValueError) as err:
            print("Could not get", url, ":", str(err))
        except Exception as err:
            raise err

# Interesting code to illustrate the purpose of the finally keyword:
def test():
    try:
        return 1
    except:
        return 2
    finally:
        return 3
# 3 is actually returned although the return statement in 1 actually executes.

import time
start_time = time.time()
max_collatz_distance(200000)
middle_time = time.time()
print(f"Non-memoized: {middle_time}")
max_collatz_distance_memo1(200000)
end_time = time.time()
print(f"Memoized: {end_time}")


