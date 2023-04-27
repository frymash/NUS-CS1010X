a = (("apple", 2), ("orange", 4), (5, 7))
b = dict(a) # b = {"apple": 2, "orange": 4, 5: 7}

c = [[1, 2], [3, 4], [5, 7]]
d = dict(c) # {1: 2, 3: 4, 5: 7}

print(b["orange"]) # 4

print(b[5]) # 7

# print(b[1]) # KeyError: there are no entries with the key 1 in b.


b["bad"] = "better"
# b = {"apple": 2, "orange": 4, 5: 7, "bad": "better"}

b[1] = "good" 
# b = {"apple": 2, "orange": 4, 5: 7, "bad": "better", 1: "good"}

for key in b.keys():
    print(key)

# apple
# orange
# 5

for val in b.values():
    print(val)

# 2
# 4
# 7

del b["bad"]
# b = {"apple": 2, "orange": 4, 5: 7, 1: "good"}
del b["apple"]
# b = {"orange": 4, 5: 7, 1: "good"}

print(tuple(b.keys()))
# ("orange", 5, 1)

print(list(b.values()))
# [4, 7, "good"]


# Question 2
def make_stack():
    stack = []
    def push_item(item):
        stack.append(item)

    def oplookup(cmd):
        nonlocal stack
        if cmd == "is_empty":
            return stack == []
        elif cmd == "clear":
            stack = []
        elif cmd == "peek":
            if stack == []:
                return "empty_stack"
            else:
                return stack[-1]
        elif cmd == "push":
            return push_item
        elif cmd == "pop":
            if stack != []:
                return stack.pop()
            else:
                return None
    return oplookup


# Question 3
def push_all(stack, seq):
    for elt in seq:
        stack("push")(elt)
    return stack


# Question 4
def pop_all(stack):
    result = []
    while not stack("is_empty"):
        result.append(stack("pop"))
    return result


# Question 5
def make_calculator(): # an RPN calculator
    stack = make_stack()
    ops = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y}
    def oplookup (msg, *args):
        # YOUR CODE BEGINS HERE
        if len(args) > 0:
            arg = args[0]
        if msg == "ANSWER":
            return stack("peek")
        elif msg == "CLEAR":
            pop_all(stack)
            return "cleared"
        elif msg == "NUMBER_INPUT":
            stack("push")(arg)
            return "pushed"
        elif msg == "OPERATION_INPUT":
            n1 = stack("pop")
            n2 = stack("pop")
            result = ops[arg](n2, n1)
            stack("push")(result)
            return "pushed"
        # YOUR CODE ENDS HERE
        else :
            raise Exception("calculator doesn't " + msg)
    return oplookup

c = make_calculator ()
print (c('ANSWER')) # empty_stack
print (c('NUMBER_INPUT',4)) # pushed
print (c('ANSWER')) # 4
print (c('NUMBER_INPUT',5)) # pushed
print (c('ANSWER')) # 5
print (c('OPERATION_INPUT','+')) # pushed
print (c('ANSWER')) # 9
print (c('NUMBER_INPUT',7)) # pushed
print (c('OPERATION_INPUT','-')) # pushed
print (c('ANSWER')) # 2
print (c('CLEAR')) # cleared
print (c('ANSWER')) # empty_stack
