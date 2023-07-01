def make_tree(entry, left, right):
    return ((entry, left, right))

def entry(tree):
    return tree[0]

def left_branch(tree):
    return tree[1]

def right_branch(tree):
    return tree[2]

def make_set():
    return ()

def is_empty_set(s):
    return s == ()

def is_element_of_set(x, s):
    if is_empty_set(s):
        return False
    elif x == entry(s):
        return True
    elif x < entry(s):
        return is_element_of_set(x, left_branch(s))
    else:
        return is_element_of_set(x, right_branch(s))

def adjoin_set(x, s):
    if is_empty_set(s):
        return make_tree(x, [], [])
    elif x == entry(s):
        return s
    elif x < entry(s):
        return make_tree(entry(s), adjoin_set(x, left_branch(s)), right_branch(s))
    else:
        return make_tree(entry(s), left_branch(s), adjoin_set(x, right_branch(s)))


def balance_tree(tree):
    ''' Homework '''
    return (tree)
