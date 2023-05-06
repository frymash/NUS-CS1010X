"""
Recap:
- A computer is made out of muliple layers.
- There is a trade-off between time and space.
- CS = data structures + algorithms

Introductory points for today:
- We should be able to live without dictionaries.
- The process of giving objects positions in dictionaries is known as hashing.
- Dictionaries consist of key-value mappings. If you know the key of a
  dictionary entry, accessing its value will take O(1) time.
- Fast access times don't come without a cost though -- dictionaries
  take up more space to allow for this.
- Dictionary collisions: 2 keys map to the same value


- Dictionaries are particularly bad for search/sort/filter/map/accumulate ops
  since the key-value mappings aren't linked to one another (unlike lists).
- Hence, when traversing the elements of a dictionary, the program will need to look
  through the empty spaces between each mapping in memory.
- The size of the empty slots in dictionaries will continually change.
- For dictionaries to reduce the possibility of collisions, the amount of memory
  allocated to it can be equivalent to 10-100x the data the dictionary needs to store
- Prof: We can live without dictionaries.

Challenge:
Implement a version of map that is similar to the stock map function in Python
(and can accept multiple collections as arguments.)

>>> tuple(map(lambda x,y: x+y, (1,2,3,4), (5,6,7,8)))
(6, 8, 10, 12)

Some languages "chain" different key-value mappings together
(like a linked list) so that traversing dictionary entries would
become faster.

Emphasis on the *
- * is used to unpack values from a collection
e.g.
>>> x = (1,2,3)
>>> print(x)
(1, 2, 3)
>>> print(*x)
1 2 3

- It can be used with a parameter in a function (e.g. *args)

"""

a = (("apple", 2), ("orange", 4), (5, 7))
b = dict(a) # b = {"apple": 2, "orange": 4, 5: 7}

# a = (("apple", 2), ("orange", 4), [5, 7], [5,99])
# b = dict(a) # b = {'apple': 2, 'orange': 4, 5: 99}
# 5:7 doesn't appear in the dictionary as every key
# can only have 1 value. 5:99 overrode 5:7 in this case.

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

# FIFO (first in first out) -> queue
# LIFO (last in first out) -> stack

# Question 2
def make_stack():
    stack = []
    def push_item(item):
        stack.append(item)

    def oplookup(cmd):
        if cmd == "is_empty":
            return stack == []
        elif cmd == "clear":
            stack.clear()
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

"""
Different implementation of make_stack() that works
if more than 1 argument is passed to oplookup.

def make_stack():
    stack = []
    def push_item(items):
        stack.extend(items)

    def oplookup(cmd, *args):
        if cmd == "is_empty":
            return stack == []
        elif cmd == "clear":
            stack.clear()
        elif cmd == "peek":
            if stack == []:
                return "empty_stack"
            else:
                return stack[-1]
        elif cmd == "push":
            return push_item(args)
        elif cmd == "pop":
            if stack != []:
                return stack.pop()
            else:
                return None
    return oplookup
"""


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
        if msg == "ANSWER":
            return stack("peek")
        elif msg == "CLEAR":
            pop_all(stack)
            return "cleared"
        elif msg == "NUMBER_INPUT":
            stack("push")(args[0])
            return "pushed"
        elif msg == "OPERATION_INPUT":
            op = args[0]
            n1 = stack("pop")
            n2 = stack("pop")
            result = ops[op](n2, n1)
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
