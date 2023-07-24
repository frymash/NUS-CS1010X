# Q1
plain = [ ['0','1','2','3','4','5'],
           ['6','7','8','9','A','B'],
           ['C','D','E','F','G','H'],
           ['I','J','K','L','M','N'],
           ['O','P','Q','R','S','T'],
           ['U','V','W','X','Y','Z'] ]

message = "HELLO 1 2 3"

def encrypt(message, plain, c1, c2): #'012345', 'ABCDEF'):
    """ (String, List[List[int or char]], String, String) -> String
    Encrypts message by converting chars from plain
    to their respective chars in the row cipher (c1)
    and the column cipher (c2)
    """
    result = ""
    for char in message:
        if char == " ":
            result += char
        else:
            for i in range(len(plain)):
                for j in range(len(plain[0])):
                        if char == plain[i][j]:
                            encrypted_char = c1[i] + c2[j]
                            result += encrypted_char
    return result

secret = encrypt(message, plain, '062849', 'abcdef')
# print(secret)

# Q2
def decrypt(secret, plain, c1, c2):
    """ (String, List[List[int or char]], String, String) -> String
    Decrypts message by converting chars from the row cipher (c1)
    and the column cipher (c2) to their respective chars in plain
    """
    result = ""
    blocks = secret.split(" ")
    for block in blocks:
        block_letters = [block[i] + block[i+1] for i in range(0, len(block)-1, 2)]
        for chunk in block_letters:
            num = chunk[0]
            char = chunk[1]
            for i in range(len(plain)):
                for j in range(len(plain[0])):
                        if num == c1[i] and char == c2[j]:
                            og_char = plain[i][j]
                            result += og_char
        result += " "
    return result[:-1]


print( decrypt(secret, plain, '062849', 'abcdef'))

# # Q3

def index(lst, char):
    """ (list of lists, int or char) -> String
    """
    def helper(lst, char):
        result = ""
        for i in range(len(lst)):
            if isinstance(lst[i], int):
                if char == lst[i]:
                    result += str(i)
            elif isinstance(lst[i], list):
                next_i = helper(lst[i], char)
                if next_i is not "":
                    result += f"{i}-{next_i}"
        return result
    final = helper(lst, char)
    return None if final == "" else final

# lst = [0,[1,2,3,4],[5,6,[7,[8,9]]]]
# for i in range(12):
#     print("index of", i, "in", lst, "is:", index(lst, i))

# # Q4 - you are not allowed to use any library functions
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
        
def make_rotation_matrix(m, n):
    """ (int, int) -> List[List[int]]
    Returns a m×n matrix where a row is the rotation (to the left)
    by 1 position of its previous row, and the first
    row is just a running number from 0 to n-1.
    """
    result = []
    to_add = [num for num in range(n)]
    for _ in range(m):
        result.append(to_add.copy())
        char_to_move = to_add.pop(0)
        # print(f"after removal: {to_add}")
        to_add.append(char_to_move)
    #     print(to_add)
    #     print(result)
    # print(f"RESULT: {result}")
    return result

# print("rotating")
# print_matrix(make_rotation_matrix(5, 5))

# # Q5
def make_symmetrical_matrix(n):
    result = []
    to_add = [num for num in range(n)]
    for element in range(1, n+1):
        result.append(to_add.copy())
        to_add.pop(-1)
        to_add.insert(0, element)
    return result

# print("symmetric")
# print_matrix(make_symmetrical_matrix(6))

# # Q6
def make_concentric_matrix(m,n):
    """ (int, int) -> Matrix
    Return a m×n matrix where the outermost ’ring’ are all zeros,
    then progressively in increasing number of
    1 then 2 in ring form into the ’center’ of the matrix.
    That is, when you connect up the same number next to each other
    (in the same row, or in two adjacent rows), you should
    see the ’ring’ for that number.
    """
    result = []
    to_add = [0]*n

    start_ind = 0
    end_ind = n-1
    curr_num = 0
    # Develop the matrix until the m//2th row
    for _ in range(m//2+1):
        result.append(to_add.copy())
        start_ind += 1
        end_ind -= 1
        curr_num += 1
        for i in range(start_ind, end_ind+1):
            to_add[i] = curr_num

    # Complete the matrix by adding rows in reverse
    if m % 2 == 0:
        result.pop()
        for sublist in result[-1::-1]:
            result.append(sublist)
    else:
        for sublist in result[-2::-1]:
            result.append(sublist)
    return result

# print("concentric")
# print_matrix(make_concentric_matrix(5,10))
# print()
# print_matrix(make_concentric_matrix(4,4))

# # Q7
def make_diamond_matrix(m,n):
    """ (int, int) -> Matrix
    """
    result = []
    if n % 2 != 0:
        to_add = [i for i in range(n//2+1)]
        to_add += to_add[-2::-1]
    else:
        to_add = [i for i in range(n//2)]
        to_add += to_add[-1::-1]     

    # Develop the matrix until the m//2th row
    for _ in range(m//2+1):
        result.append(to_add)
        to_add = list(map(lambda x: x+1, to_add))
    
    # Complete the matrix by adding rows in reverse
    if m % 2 == 0:
        result.pop()
        for sublist in result[-1::-1]:
            result.append(sublist)
    else:
        for sublist in result[-2::-1]:
            result.append(sublist)
    return result

print("diamond")
# print_matrix(make_diamond_matrix(7,7))
# print()
# print_matrix(make_diamond_matrix(8,7))
# print()
# print_matrix(make_diamond_matrix(8,8))
# print()
# print_matrix(make_diamond_matrix(7,8))


# # Q8 - Q10
class Node(object):
    def __init__(self, num, before, after, top, bottom):
        self.num = num
        self.before = before    # node before the current node
        self.after = after      # node after the current node
        self.top = top          # its copy above the current layer
        self.bottom = bottom    # a copy below the current layer

def insert_into(head, num):
    if head == None:
        # this is the very first node in the list
        return Node(num, None, None, None, None)

    previous = None
    current = head
    while current != None:
        if num < current.num:
            # insert newNode before the current node
            newNode = Node(num, previous , current, None, None)
            if previous != None:
                previous.after = newNode
            if current.before == None:
                head = newNode
            current.before = newNode
            return head
        previous = current
        current = current.after
    # insert newNode after the last node in the current list
    newNode = Node(num, previous, None, None, None)
    previous.after = newNode
    return head

# Q8
def all_keys(node):
    """ (Node) -> String
    """
    result = ""
    while node.after != None:
        result += (str(node.num) + "-")
        node = node.after
    result += str(node.num)
    return result

lst = None
for i in [4,3,16,14,24,2,5,22,17,9,1,6,11,7,18,12,13]:
    lst = insert_into(lst, i)

# Q9
def search_layer(node, num):
    """ (Node) -> String
    """
    result = ""
    while node.after != None:
        # print(f"node.num: {node.num}")
        # print(f"num: {num}")
        if node.num == num or num < node.num:
            break
        result += (str(node.num) + "-")
        node = node.after
    result += str(node.num)
    return result

print("Current full list is:", all_keys(lst))
for i in range(1,27,5):
    print("visited nodes in searching for", i, ":", search_layer(lst, i))

# print("visited nodes in searching for", i, ":", search_layer(lst, 1))

# # Q10
import random
random.seed(1)          # let's use this seed for our testing
# input is a non-empty lst with the first element always smallest
def create_top(lst):
    topLst = Node(lst.num, None, None, None, lst)
    previous = topLst
    current = lst.after
    while current != None:
        rand = random.randint(0, 10)
        # print(f"rand: {rand} | current.num: {current.num} | previous.num: {previous.num}")
        if rand <= 3:
            newNode = Node(current.num, previous, None, None, current)
            previous.after = newNode
            current.top = newNode
            # print(f"previous.after.num: {previous.after.num} | current.top.num: {current.top.num}\n")
            previous = newNode
        current = current.after
    return topLst

topLst = create_top(lst)
print("Current topLst:", all_keys(topLst))

topMostLst = create_top(topLst)

print("Current topMostLst:", all_keys(topMostLst))


def search(topMostLst, num):
    if type(topMostLst) != Node:
        return ""
    
    visited = []
    curr = topMostLst
    while True:
        if curr.num == num:
            visited.append(curr.num)
            break
        elif curr.num < num:
            visited.append(curr.num)
            if curr.after:
                curr = curr.after
            elif curr.before:
                curr = curr.before
            else:
                break
        else: # num < curr.num
            if curr.before and curr.before.bottom:
                curr = curr.before.bottom
            else:
                visited.append(curr.num)
                break
    return visited
    # return "-".join(map(str, sorted(set(visited))))
            

# for i in range(25):
#     print("searching using 1 list", i, ":", search(lst, i))    

# for i in range(25):
#     print("searching using 2 lists", i, ":", search(topLst, i))    

for i in range(25):
   print("searching using 3 lists", i, ":", search(topMostLst, i))





