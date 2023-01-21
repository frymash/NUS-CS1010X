#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: O(4^n * n^2)

# n * 3^n
# Ans: O(n * 3^n)

# 1000000000n^2
# Ans: O(n^2)

# 2^n/1000000000
# Ans: O(2^n)

# n^n + n^2 + 1
# Ans: O(n^2)

# 4^n + 2^n
# Ans: O(4^n)

# 1^n
# Ans: O(1)

# n^2
# Ans: O(n^2)

# Faster order of growth in each group:

# i. O(4^n * n^2) 
# ii. O(2^n/1000000000)
# iii. O(4^n + 2^n)
# iv. O(n^2)


##########
# Task 2 #
##########

# bar runs in O(n) time and occupies O(n) space
#
# The return statement for foo multiplies a constant n
# by bar(n) (O(n) time, O(n) space).
# Since * runs in O(1) time and occupies O(1) space,
# the return statement will run in O(1 * n) = O(n) time
# and occupy O(n) space.

# Time complexity: O(n)
# Space complexity: O(n)


##########
# Task 3 #
##########

# Time complexity of bar: O(n)
# Time complexity of foo: O(n^2)


# Space complexity of bar: O(n)
# Space complexity of foo: O(n)

# O(1) time, O(1) space
def improved_bar(n):
    """ Returns the sum of all positive integers up to n
    with the use of the AP sum formula

    S_n = n/2 * [2*a + (n−1) * d]

    where n = the argument passed to parameter n,
          a = 1,
          d = 1

    int -> int
    """
    return int(n/2 * (2+(n-1)))

# O(n) time, O(1) space
def improved_foo(n):
    """ Returns bar(n) + bar(n-1) + bar(n-2) + ... + bar(0)

    int -> int
    """
    result = 0
    for number in range(1,n+1):
        result += improved_bar(number)
    return result


# Improved time complexity: O(n)
# Improved space complexity: O(1)


'''
# For testing:

def bar(n):
    if n == 0:
        return 0
    else:
        return n + bar(n - 1)

def foo(n):
    if n == 0 :
        return 0
    else:
        return bar(n) + foo(n - 1)

def test_suite():
    successes = 0
    failures = 0

    def int_function_test(func, n, actual_ans):
        """ Test framework for 1-arg functions with input type int and return type int.

        (int -> int) * int * int -> None
        """
        ans = func(n)
        print(f"{func.__name__}({n}) == {actual_ans}: {ans == actual_ans} (type: {type(ans)})")
        if ans == actual_ans:
            nonlocal successes
            successes += 1
        else:
            nonlocal failures
            failures += 1

    def improved_bar_test(n, actual_ans):
        return int_function_test(improved_bar, n, actual_ans)

    def improved_foo_test(n, actual_ans):
        return int_function_test(improved_foo, n, actual_ans)
    
    def improved_bar_tests():
        improved_bar_test1 = improved_bar_test(0,0)
        improved_bar_test2 = improved_bar_test(5, 15)
        improved_bar_test3 = improved_bar_test(10, 55)
        improved_bar_test4 = improved_bar_test(10, 55)
        print("improved_bar_tests complete\n")

    def improved_foo_tests():
        improved_foo_test1 = improved_foo_test(0,0)
        improved_foo_test2 = improved_foo_test(5,35)
        improved_foo_test3 = improved_foo_test(10,220)
        improved_foo_test4 = improved_foo_test(32,5984)
        improved_foo_test5 = improved_foo_test(100,171700)
        print("improved_foo_tests complete\n")

    improved_bar_tests()
    improved_foo_tests()
    print(f"{successes} tests passed, {failures} tests failed.")

test_suite()
'''
