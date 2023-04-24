# Question 1
def make_widget():
    stuff = ["empty", "empty", 0]
    def oplookup(msg,*args):
        if msg == "insert":
            place = stuff[2]
            stuff[place] = args[0]
            stuff[2] = (place + 1) % 2
        elif msg == "retrieve":
            return stuff[stuff[2]]
        elif msg == "stuff":
            return stuff
        else:
            raise Exception("widget doesn’t " + msg)
    return oplookup

widget = make_widget()

# (a)
# A widget object can store 2 items.
# You can interact with a widget object in 2 ways:
# 1. You can ask it to insert a new item into its storage.
#    That item will replace the oldest item in storage.
# 2. You can also ask it to retrieve the oldest item in storage. 

# (b)
widget("insert", 1)
widget("insert", 2)
widget("insert", 3)

# (c)
# 2 will always be returned as it will remain the oldest item in storage
# no matter how many retrievals you make (as long as no insertions are
# made in between retrievals).


# Question 2
def make_accumulator():
    result = 0
    def accumulate(n):
        nonlocal result
        result += n
        return result
    return accumulate

# Question 3

# Question 4
