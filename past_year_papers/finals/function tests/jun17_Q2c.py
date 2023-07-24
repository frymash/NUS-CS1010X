def make_memo_fib():
    memo = {}
    largest = [-1]
    def helper(n):
        if n in memo:
            return memo[n]
        elif largest[0] >= n:
            return False
        a,b = 0,1
        while a <= n:
            memo[a] = True
            if a == n:
                return True
            a,b = b, a+b
        largest[0] = n
        return False
    return helper

# a = [1,2,4,1,11,6,7,9,23,5,8,13]
# print(list(filter(make_memo_fib(), a)))

def tree_scale(tree, factor):
    def scale_fn(subtree):
        if type(subtree) != tuple:
            return factor*subtree
        else:
            return tree_scale(subtree, factor)
    return tuple(map(scale_fn, tree))
    
print(tree_scale(((1,2),(3,4), 5), 2))