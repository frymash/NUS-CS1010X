#----------------
#    TOPIC 1
#----------------

# Question 1

def record(f):
    """Please do not paste the record function to Coursemology"""
    def helper(*args):
        global count
        count += 1
        return f(*args)
    return helper

@record # include this line in your submission
def jump_locate(aList, begin, end, jump, num_to_find):
    if begin+jump > end:
        return "Not Found"
    elif aList[begin] == num_to_find:
        return begin
    else: # 
        check = aList[begin+jump]
        if check == num_to_find:
            return begin + jump
        elif check < num_to_find:
            # if not begin+jump+1 <= check <= end:
            #     return "Not Found"
            new_begin = begin+jump+1
            new_jump = jump*2
            if new_begin + new_jump > end:
                new_jump = end - new_begin
            return jump_locate(aList, new_begin, end, new_jump, num_to_find)
        else: # check > num_to_find
            return jump_locate(aList, begin+1, begin+jump-1, 1, num_to_find)
    

count = 0
print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1001)) # 500
print(count) # 34

count = 0
print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1000)) # 'Not Found'
print(count) # 35


#----------------
#    TOPIC 2
#----------------

def print_tree(tree):
    """Function to print a binary tree in friendly format. Do not modify and do not submit to Coursemology."""
    def to_str(tree):
        if tree == ():
            return [], 0, 0
        if tree[1] == () and tree[2] == ():
            _lst = [f'({tree[0]:03d})']
            return _lst, 5, 2
        ltree, lwidth, lpos = to_str(tree[1])
        rtree, rwidth, rpos = to_str(tree[2])
        _lst = [' ' * lwidth + f'({tree[0]:03d})' + ' ' * rwidth]
        line = (' ' * lpos + '+' + '-' * (lwidth - lpos + 1) + '+' if lwidth else '  +') \
            + ('-' * (rpos + 2) + '+' + ' ' * (rwidth - rpos - 1) if rwidth else '  ')
        _lst.append(line)
        for i in range(max(len(ltree), len(rtree))):
            line = (ltree[i] if i < len(ltree) else ' ' * lwidth) + ' ' * 5 \
                + (rtree[i] if i < len(rtree) else ' ' * rwidth)
            _lst.append(line)
        return _lst, len(_lst[0]), lwidth + 2
    try:
        lst = to_str(tree)[0]
        for s in lst:
            print(s)
    except:
        print('Something went wrong. Your input might be invalid.')

# iTupleList is just a list of public test cases for your convenience
iTupleList = []
iTupleList.append(((8, -1, 6), (7, 4, 9), (5, 1, 2), (1, 7, -1), (2, 3, 8), (3, -1, 0)))
iTupleList.append(((0, 1, 2),))
iTupleList.append(((0, 2, -1), (1, 0, -1)))
iTupleList.append(((2, -1, 0), (0, -1, 1)))
iTupleList.append(((0, 3, 2), (1, 4, 0)))

# Question 2

def find_root(iTuple):
    """ (iTuple) -> int
    
    Returns the root of the binary tree
    """
    candidates = list(map(lambda node: node[0], iTuple))
    flatten = []
    for node in iTuple:
        # print(node)
        flatten.append(node[0])
        flatten.append(node[1])
        flatten.append(node[2])
    candidates = list(filter(lambda node: flatten.count(node) == 1, candidates))
    return candidates[0]

# for iTuple in iTupleList:
#     print(find_root(iTuple))

# Question 3

def binary_tree(iTuple):
    tree_copy = iTuple
    root = find_root(iTuple)
    result = (root,)
    
    # Find root leaves
    left = ...
    right = ...
    left_subtree = binary_tree
    
    # Recursively develop left and right subtrees
    
    

# for iTuple in iTupleList:
#     tree = binary_tree(iTuple) 
#     print(tree)
#     print_tree(tree)


#----------------
#    TOPIC 3
#----------------

# Question 4

class Tribes():
    def __init__(self, N):
        # Use a dictionary to capture the leader for each of the N tribes
        self.leaders = {}
        for i in range(1, N+1):
            self.leaders[i] = i

    def tribe_leader(self, A):
        # Find the leader of tribe A, which is A if no one has conquered it before,
        # or ... (this is related to what you do for the next function, conquer)
        return self.leaders[A]

    def conquer(self, A, B):
        # Purpose: Tribe A conquers tribe B
        # If tribe A conquers tribe B, any tribe conquered by tribe B
        # will then be led by A's leader as well
        prev_B_leader = self.leaders[B]
        new_B_leader = self.leaders[A]
        self.leaders[B] = new_B_leader
        for tribe in self.leaders:
            if self.leaders[tribe] == prev_B_leader:
                self.leaders[tribe] = new_B_leader

    def is_same_tribe(self, A, B):
        return self.leaders[A] == self.leaders[B]

def testTribes():
    N = 100
    T = Tribes(N)
    T.conquer(10, 20)
    print(T.tribe_leader(20))
    print(T.is_same_tribe(20, 11))
    T.conquer(5, 10)
    T.conquer(10, 11)
    print(T.is_same_tribe(20, 11))

testTribes()


#----------------
#    TOPIC 4
#----------------

# Question 5

def nodes_in_subtree(tree, root, child):
    pass

"""
def subtree_distance(tree):
    # Base case: leaf
    if len(tree) - tree.count(False) == 1:
        return 0
    else:
        root = tree.index(-1) # 0
        root_children = [] # [1,2]
        for i in range(len(tree)):
            if tree[i] == root:
                root_children.append(i)
        left_child = root_children[0]
        right_child = root_children[1]
                
        # Create left subtree
        left = []
        
        
        # Create right subtree
        right = []
        
        return 1 + max(subtree_distance(left), subtree_distance(right)
        """

# print(subtree_distance([-1, 0, 0, 1, 2, 2, 5]))

# Question 6

def tree_distance(tree):
    pass

# print(tree_distance([-1, 0, 0, 1, 2, 2, 5]))
# print(tree_distance([-1, 0, 0, 1, 2, 3, 4]))


#----------------
#    TOPIC 5
#----------------

# Question 7
def count_bugles(n, m):
    if n < m:
        return count_bugles(m, n)
    if n == 2 and m == 0:
        return 4
    else:
        largest_bugle_side_length = n
        

# print(count_bugles(3, 3))
# print(count_bugles(4, 5))
