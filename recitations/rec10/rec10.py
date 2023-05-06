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

# Memoized implementation of fib runs in O(n) time
# Table lookup should be O(1). 
# Think: How will the time complexity of fib change
# if the table lookup time becomes O(n)?
def memo_fib(n):
    def helper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return memo_fib(n-1) + memo_fib(n-2)
    return memoize(helper, "memo_fib")(n)

# Time complexity: exponential
def choose(n,k):
    if k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    else:
        return choose(n-1, k) + choose(n-1, k-1)
    
# Memoized version of choose
def memo_choose(n,k):
    def helper(n,k):
        if k > n:
            return 0
        elif k == 0 or k == n:
            return 1
        else:
            return memo_choose(n-1, k) \
                   + memo_choose(n-1, k-1)
    return memoize(helper, "choose")(n,k)