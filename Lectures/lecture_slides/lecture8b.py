#############################################
#
# from Lecture 8a part of the video
#
#############################################
def filter(predicate, seq):
    if seq == ():
        return ()
    else:
        if predicate(seq[0]):
            return (seq[0],) + filter(predicate, seq[1:])
        else:
            return filter(predicate, seq[1:])

def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

def map(fn, seq):
    if seq == ():
        return ()
    else:
        return (fn(seq[0]), ) + map(fn, seq[1:])
    
#############################################
#
# working with tree: a sequence of sequences
#
#############################################

#
# Eg 4: count_leaves
#
print("Example 4: count_leaves")
def count_leaves(tree):
    if tree == ():
        return 0
    elif type(tree) != tuple:
        return 1
    else:
        return count_leaves(tree[0]) + \
               count_leaves(tree[1:])

tree = ( (1,2), (3,4), 5 )
print( count_leaves( tree ) )
print( count_leaves( tree + tree ) )
tree =( (1,2), (3,4), tree)
print( count_leaves(tree) )
print( count_leaves(tree + tree))

#
# Eg 5: tree_flatten
#
print("")
print("Example 5: tree_flatten")
def tree_flatten(tree):
    if tree == ():
        return ()
    elif type(tree) != tuple:
        return (tree,)
    else:
        return tree_flatten(tree[0]) + tree_flatten(tree[1:])

tree = ( (1,2), (3,4), 5)
print(len(tree_flatten(tree)))
print(len(tree_flatten(tree + tree)))
tree =( (1,2), (3,4), tree)
print(len(tree_flatten(tree)))
print(len(tree_flatten(tree + tree)))

#
# Eg 6: sum_odd_square(tree)
#
print("")
print("Example 6: sum_odd_square")
def sum_odd_square(tree):
    return accumulate(lambda x,y: x+y, 0,
                      map(lambda x: x**2,
                          filter(lambda x: x%2, tree_flatten(tree))))

tree = ( (1,2), (3,4), 5)
print(sum_odd_square(tree))
tree =( (1,2), (3,4), tree)
print(sum_odd_square(tree))

#
# Eg 7: tree_scale
#
# Eg 7, attempt #1
#
print("")
print("Example 7: tree_scale (attempt #1): commented out due to error")
def tree_scale(tree, factor):
    if tree == ():
        return ()
    elif type(tree) != tuple:
        return tree*factor
    else:
        return tree_scale(tree[0], factor) + tree_scale(tree[1:], factor)


#tree = ( (1,2), (3,4), 5)
#print(tree_scale(tree, 2))

#
# Eg 7, attempt #2, does not maintain the hierarchy of a tree - not correct
#
print("")
print("Example 7: tree_scale (attempt #2): does not maintain the hierarchy of a tree")
def tree_scale(tree, factor):
    if tree == ():
        return ()
    elif type(tree) != tuple:
        return (tree*factor, )
    else:
        return tree_scale(tree[0], factor) + tree_scale(tree[1:], factor)

tree = ( (1,2), (3,4), 5)
print(tree_scale(tree, 2))

#
# Eg 7, attempt #3: okay version,
#       map itself has takken care of the "()" needed to put the answer to maintain the tree hierarchy
#
#
print("")
print("Example 7: tree_scale (attempt #3)")
def tree_scale(tree, factor):
    def scale_fn(subtree):
        if type(subtree) != tuple: # is_leaf
            return factor * subtree
        else:
            return tree_scale(subtree, factor)
    return map(scale_fn, tree)

tree = ( (1,2), (3,4), 5)
print(tree_scale(tree, 2))

#
# Example 8: tree_copy
#
# not the correct version
def tree_copy(tree):
    return tree

# the correct version
print("")
print("Example 8: tree_copy")

def tree_copy(tree):
    return tree_scale(tree, 1)


def tree_copy(tree):
    def copy_fn(subtree):
        if not type(subtree) == tuple: # can check for list if using Python map instead of own map
            return subtree
        else:
            return tree_copy(subtree)
    return map(copy_fn, tree)  # if using Python map, we can allow tree to have the list representation too

tree = ( (1,2), (3,4), 5)
w = tree_copy(tree)
print(w, "w is the identical tree to the given:", w is tree)  # False
print(w, "w is the equivalent to the given:", w == tree) # True

#
# Example 9: tree_map
#
print("")
print("Example 9: tree_map")
def tree_map ( fn, tree):
    def mapping_fn(subtree):
        if type(subtree) != tuple:
            return fn(subtree)
        else:
            return tree_map(fn, subtree)
    return map(mapping_fn, tree)

# tree_copy
def tree_copy(tree):
    return tree_map(lambda x:x, tree)

print("A: tree_map to get tree_copy")
tree = ( (1,2), (3,4), 5)
t1 = tree_map ( lambda x: x, tree)
print(t1, "t1 is the identical tree to the given:", t1 is tree)  # False
print(t1, "t1 is the equivalent to the given:", t1 == tree) # True
t2 = tree_copy (tree)
print(t2, "t2 is the identical tree to the given:", t2 is tree)  # False
print(t2, "t2 is the equivalent to the given:", t2 == tree) # True


# tree_scale
print("")
print("B: tree_map to get tree_scale")

def tree_scale(tree, factor):
    return tree_map(lambda x: x*factor, tree)

t2 = tree_map(lambda x: x*3, tree)
print(t2)
t2 = tree_scale(tree, 3)
print(t2)


#
# Example 10: tree_accumulate vs accumulate
#
print("")
print("Example 10: tree_accumulate")
def tree_accumulate(fn, initial, tree):
    return accumulate(lambda x,y: x+y, initial,
                      map(fn,
                          tree_flatten(tree)))

tree = ((1,2), (3,4), 5)
print( tree_accumulate(lambda x:x*x, 0, tree))

#
# Example 11: tree_filter vs filter
#

# ?? how to do ??

#########################################################
#
# Recap recursion vs iteration
#
#########################################################
#
# recap Eg 4
#
print("")
print("Recap recursion vs iteration")
print("Recap Eg 4: count_leaves")
def count_leaves(tree):
    if tree == ():
        return 0
    result = 0
    stack = tree  # tree is a tuple
    while stack != ():
        # print(stack, "<-- in stack")                                              # uncomment this to see the stack's content
        if type(stack[0]) != tuple:     # is_leaf
            result += 1
            stack = stack[1:]           # pop the top of the stack
        else:
            items = stack[0]            # assign the top of the stack to items
            stack = stack[1:]           # remove the top of the stack
            for i in items[-1::-1]:     # unpack each child in items 
                stack = (i, ) + stack   #                   to put into the stack
    return result

tree = ( (1,2), (3,4), 5 )
print( count_leaves( tree ) )
print( count_leaves( tree + tree ) )
tree =( (1,2), (3,4), tree)
print( count_leaves(tree) )
print( count_leaves(tree + tree))

#
# recap Eg 5
#
print("")
print("Recap recursion vs iteration")
print("Recap Eg 5: tree_flatten")
def tree_flatten(tree):
    if tree == ():
        return ()
    result = ()
    stack = tree  # tree is a tuple
    while stack != ():
        #print(stack, "<-- in stack   ", result, "<-- in result")
        if type(stack[0]) != tuple: # is_leaf
            result = result + (stack[0],)
            stack = stack[1:]
        else:
            items = stack[0]
            stack = stack[1:]
            for i in items[-1::-1]:
                stack = (i, ) + stack
    return result

tree = ( (1,2), (3,4), 5)
print(len(tree_flatten(tree)))
print(len(tree_flatten(tree + tree)))
tree =( (1,2), (3,4), tree)
print(len(tree_flatten(tree)))
print(len(tree_flatten(tree + tree)))

#
# recap Eg 7: buggy codes
#
print("")
print("Recap recursion vs iteration")
print("Recap Eg 7: tree_copy....not a correct version")
def tree_copy(tree):
    if tree == ():
        return ()
    result = ()
    #stack = (tree, "#")  # tree is a tuple
    stack = tree
    while stack != ():
        print(stack, "<-- in stack   ", result, "<-- in result")
        if type(stack[0]) != tuple: # is_leaf or marker
            if stack[0] == "#":
                result = (result,)
            else:
                result = result + (stack[0],)
            stack = stack[1:]
        else:
            items = stack[0]
            stack = ("#",) + stack[1:] 
            for i in items[-1::-1]:
                stack = (i, ) + stack
    return result

tree = ( (1,2), (3,4), 5)
print(tree_copy(tree))




    
