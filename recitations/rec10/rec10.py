"""
Why is it good to study dynamic programming?
- A way to think about solving problems

Other problem solving methods:
- Divide and conquer (merge sort)
- Plane sweep

Can we use big-O notation to account for the space occupied by
a dictionary during a memoization op?
- No, because a dictionary is typically allocated significantly more memory
  than the amount it requires.
- This also means that in exchange for the quick access times that dictionaries
  guarantee us, we need to use up more space.

DP is a bottom-up approach to problem-solving.
It uses a nested loop to "fill up the blanks" in a table.

Is memoization or DP faster?
- One could say memoization is faster as it only performs the computations we need
  and ensures that we don't perform the same computation multiple times.
- However, DP systematically fills up a table (with entries that we don't actually
  need) and combines entries in that table to help us get our final answer.

"""

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

# Dynamic programming version of choose
def dp_choose(n,k):
    row = [1] * (k+1)
    table = []

    # Enumerate table with n rows of k 1s
    for i in range(n+1):
        table.append(row.copy())

    # Fill first row with 0s
    for j in range(1, k+1):
        table[0][j] = 0
    
    # Main choose algorithm; combine the k and k-1th element
    # from the i-1th row
    for i in range(1, n+1):
        for j in range(1, k+1):
            table[i][j] = table[i-1, k] \
                          + table[i-1, k-1]
    return table[n][k]


# Question 1a: Counting change with memoization

kind_of_coins = (1,5,10,20,50)
cc_rec_calls = 0
    
def cc(amount, num_of_coins):
    global cc_rec_calls
    cc_rec_calls += 1
    current_denom = kind_of_coins[num_of_coins-1]
    if amount < 0 or num_of_coins == 0:
        return 0
    elif amount == 0:
        return 1
    else:
        return cc(amount - current_denom, num_of_coins) \
               + cc(amount, num_of_coins - 1)

print(cc(11, 5))
print(f"Number of recursive calls made by cc: {cc_rec_calls}")

memoize_cc_rec_calls = 0
def memoize_cc(amount, num_of_coins):
    def helper(amount, num_of_coins):
        global memoize_cc_rec_calls
        memoize_cc_rec_calls += 1
        current_denom = kind_of_coins[num_of_coins-1]
        if amount < 0 or num_of_coins == 0:
            return 0
        elif amount == 0:
            return 1
        else:
            return memoize_cc(amount - current_denom, num_of_coins) \
                   + memoize_cc(amount, num_of_coins - 1)
    return memoize(helper, "cc")(amount, num_of_coins)

print(memoize_cc(11, 5))
print(f"Number of recursive calls made by memoize_cc: {memoize_cc_rec_calls}")

"""
count = 0
seen = []
def memo_cc(a,d):
    global count
    count += 1
    if (a,d) in seen:
        return seen[(a,d)]
"""


# Question 1b: Counting change with DP

def dp_cc(amount, num_of_coins):
    # +1 to account for num_of_coins == 0
    row = [1] * (num_of_coins + 1)
    table = []

    # DO NOT INITIALIZE THE TABLE USING A LIST COMPREHENSION
    # OTHERWISE EVERY ROW WILL POINT TO THE SAME REFERENCE IN MEMORU
    # table = [row for i in range(amount+1)]

    for i in range(amount+1):
        table.append(row.copy())

    # Replace 1st value of each row with 0
    for row in table:
        row[0] = 0

    print(table)

    # Main cc mechanism
    # Each call to dp_cc consists of 2 sub-cases:
    # Case 1: Deduct largest denom from amount. Number of coins remains the same.
    # Case 2: Amount remains the same. Deduct 1 coin from the number of coins.
    # (this will be the largest denom)
    for i in range(amount+1):
        for j in range(num_of_coins+1):

            # Account for case 1
            highest_denom = kind_of_coins[j-1]
            new_amount = i - highest_denom
            #print(f"highest_denom: {highest_denom}")
            if new_amount < 0:
                case1 = 0
            elif new_amount == 0:
                case1 = 1
            else:
                case1 = table[new_amount][j]

            # Account for case 2
            new_num_of_coins = j-1
            if new_num_of_coins <= 0:
                case2 = 0
            else:
                case2 = table[i][new_num_of_coins]

            table[i][j] = case1 + case2
            #print(f"\ncc({i},{j}): {table[i][j]}")
            #print(f"case 1: cc({new_amount},{j})")
            #print(f"case 2: cc({i},{new_num_of_coins})")
    for i in range(len(table)):
        print(f"{i}: {table[i]}")
                
    return table[amount][num_of_coins]

print(dp_cc(11,5))

"""
Prof's solution:

def cc(a,d):
    oneline = [0] * (d+1)
    for i in range(a+1):
        table.append(list(oneline))
    for i in range(1, d+1):
        table[0][i] = 1
        
    for col in range(1, d+1):
        for row in range(1, a+1):
            if row - kind_of_coins[col-1] < 0:
                ans1 = 0
            else:
                ans1 = table[row - coins[col-1][col]]
            table[row][col] ans1 + table[row][col-1]
    return table

TA's solution during tutorial 10:

def coins(n):
    return (1,5,10,20,50)[n-1]

def dp_cc(a, n):
    table = [[0]*n for _ in range(a+1)]
    # base cases
    for j in range(n):
        table[0][j] = 1

    for i in range(1, a+1):
        for j in range(n):
            x = table[i-coins(j+1)[j] if i-coins(j+1) >= 0 else 0]
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y

    return table[a][n-1]

print(dp_cc(200,5))
"""
        
    

# Question 2a: cut_rod with recursion

prices = {1:1, 2:5, 3:8, 4:9, 5:10 , 6:17 , 7:17 , 8:20 , 9:24 , 10:30}

def cut_rod(n, prices):
    if n <= 0:
        return 0
    else:
        max_price = 0
        for p in prices:
            if p <= n:
                max_price = max(max_price, prices[p] + cut_rod(n-p, prices))
            # print(f"p = {p} | max_price: {max_price}")
        return max_price

print(cut_rod(10, prices))

# Question 2b: cut_rod with DP

def dp_cut_rod(n, prices):
    max_price = []
    row = [0] * (len(prices)+1)
    for i in range(n+1):
        max_price.append(list(row))

    for length in range(1, n+1):
        for p in range(1, len(prices)+1):
            if p <= length:
                max_price[length][p] = max(max_price[length][p-1], prices[p] + max_price[length-p][p])
            else:
                max_price[length][p] = max_price[length][p-1]
    return max_price[n][len(prices)]

print(dp_cut_rod(10, prices))
            
                
