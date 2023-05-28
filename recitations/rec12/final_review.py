# Q1

def deep_reverse(lst):
    if lst == []:
        return []
    else:
        result = []
        for i in range(len(lst),0,-1):
            if type(lst[i]) == list:
                to_add = deep_reverse(lst[i])
            else:
                to_add = lst[i]
            result.append(to_add)
        return result
    
def deep_reverse(a):
    if a == []:
        return []
    elif type(a[0]) == list:
        return deep_reverse(a[1:]) + [deep_reverse(a[0])]
    else:
        return deep_reverse(a[1:]) + [a[0]]
    
def deep_sum(a):
    if a == []:
        return 0
    elif type(a[0]) == list:
        return deep_sum(a[1:]) + [deep_sum(a[0])]
    else:
        return deep_sum(a[1:]) + [a[0]]
    
# Q2
# (5 * 4) + (2 - 1)
# = 20 + (2-1)
# = 20 +1
# = 21
# For prefix, order of ops: + * 5 4 - 2 1
# Prefix notation is used in Lisp-like languages
# For postfix, order of ops: 5 4 * 2 1 - +

# def make_stack():
#     def helper(msg, *args):
        
#     return helper

def prefix_infix(a):
    op_s = make_stack()
    for op in a:
        if op in ['*', '/', '+', '-'] or op_s("peek") in ['*', '/', '+', '-']:
            op_s("push", str(op))
        else:
            op_s("push", "(" + op_s("pop") + op_s("pop") + str(op) + ")")
            while op_s("size") > 0 and op_s("peek") not in ['*', '/', '+', '-']:
                temp = "(" + op_s("pop") + op_s("pop") + temp + ")"
            op_s("push", temp)
    while op_s("size") > 1:
        back = op_s("pop")
        front = op_s("pop")
        op_s("push", "(" + front + op_s("pop") + back + ")")
    return op_s("pop")

# Q3
"""
print(enumerate_interval(1,8))
print(map(lambda x: 5*x, enumerate_interval(1,12)))
print(map(lambda x: x*x, filter(lambda x: x%2, enumerate_interval(1,11))))
print(map(lambda x: x*x if x%2 else x//2, enumerate_interval(1,10)))
s = filter(lambda x: x%2==0 and x%6!=0, enumerate_interval(1,20))
s.reverse()
print(s)
"""

# Q4

from math import log

def power_set(a):
    if a == []:
        return [[]]
    else:
        result1 = power_set(a[1:])
        result2 = list(map(lambda x: x+[a[0]], result1))
        print(f"result1: {result1}")
        print(f"result2: {result2}\n")
        return result2 + result1
    
def power_set_check(a):
    size = int(log(len(a),2))
    if 2**size != len(a):
        return False
    check = []
    for i in a:
        if len(i) == size:
            check = power_set(i)
            break
    
    # now i has a power set to be compared with the input set
    for j in a:
        j.sort()
    
    for i in check:
        i.sort()
        if i not in a:
            return False
    
    return True

# Q5

class Number(object):
    def __init__(self,num):
        self.num = num

    def value(self):
        return self.num
    
    def minus(self, amt):
        if self.value() == "Undefined" or amt.value() == "Undefined":
            return (Number("Undefined"))
        return Number(self.value() - amt.value())
    
    def plus(self, amt):
        if self.value() == "Undefined" or amt.value() == "Undefined":
            return (Number("Undefined"))
        return Number(self.value() + amt.value())
    
    def times(self, amt):
        if self.value() == "Undefined" or amt.value() == "Undefined":
            return (Number("Undefined"))
        return Number(self.value() * amt.value())
    
    def divide(self, amt):
        if self.value() == "Undefined" or amt.value() == "Undefined":
            return (Number("Undefined"))
        if amt.value() == 0:
            return (Number("Undefined"))
        return Number(self.value() / amt.value())
