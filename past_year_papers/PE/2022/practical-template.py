################################################################
#                           TOPIC 1                            #
################################################################

## Question 1 ##
from string import ascii_uppercase

def encrypt(message, cipher):
    """ (String, String) -> String
    """
    result = ""
    plain = list(ascii_uppercase)
    for char in message:
        if char == " ":
            result += char
        else:
            # Find index of char in plain and extract cipher char from same index
            i = plain.index(char)
            encrypted_char = cipher[i]

            # Add char to result
            result += encrypted_char
           
            # Move char from plain to front of plain
            plain.insert(0, plain.pop(i))
            # print(plain)

    return result
    
    

#print("*** Question 1 ***")
#print(encrypt('HELLO', 'DEFGHIJKLMNOPQRSTUVWXYZABC') == 'KIODR', encrypt('HELLO', 'DEFGHIJKLMNOPQRSTUVWXYZABC'))
#print(encrypt('I LOVE PYTHON', 'DQOLVJSGYCREUTBKXIWNHAMZPF') == 'Y EBAY XPABSW', encrypt('I LOVE PYTHON', 'DQOLVJSGYCREUTBKXIWNHAMZPF'))


## Question 2 ##
#1. Create a reversed message
#2. For each char in the reversed message, move the char back to its original position in plain
#

def decrypt(message, cipher):
    """ (String, String) -> String
    """
    result = ""
    plain = list(ascii_uppercase)
    for char in message:
        if char == " ":
            result += char
        else:
            # Find index of char in plain and extract cipher char from same index
            i = cipher.index(char)
            actl_char = plain[i]

            # Add char to result
            result += actl_char
               
            # Move char from plain to front of plain
            plain.insert(0, plain.pop(i))
            # print(plain)
    return result

#print("\n*** Question 2 ***")
#print(decrypt('KIODR', 'DEFGHIJKLMNOPQRSTUVWXYZABC') == 'HELLO', decrypt('KIODR', 'DEFGHIJKLMNOPQRSTUVWXYZABC'))
#print(decrypt('Y EBAY XPABSW', 'DQOLVJSGYCREUTBKXIWNHAMZPF') == 'I LOVE PYTHON', decrypt('Y EBAY XPABSW', 'DQOLVJSGYCREUTBKXIWNHAMZPF'))


## Question 3 ##


def decrypt_wbw(message, cipher):
    """ (String, String) -> String

    Decrypts a message word by word.

    1. Decrypts the 1st word without changing the plain-cipher mapping
    2. After the 1st word is decrypted, letters from the 1st word will be
    shifted to the head of plain
    3. Repeat steps 1-2 until every word in the message is encrypted.
    
    """
    split_msg = message.split()
    result = ""
    plain = list(ascii_uppercase)
    actl_word = ""
    
    for codeword in split_msg:
        for char in codeword:
            # Find index of char in plain and extract cipher char from same index
            i = cipher.index(char)
            actl_char = plain[i]

            # Add char to result
            result += actl_char
            actl_word += actl_char

        # Add spacing behind word
        result += " "

        # Take the letters in the word and shift them to the front of plain
        letters = sorted(list(set(actl_word)))
        for char in letters:
            i = plain.index(char)
            plain.pop(i)
        plain = letters + plain
        actl_word = ""

    # Get rid of the additional space at the end of the last word
    return result[:-1]
    

#print("\n*** Question 3 ***")
#print(decrypt_wbw('KHOOR QHOGU PQKLIHW', 'DEFGHIJKLMNOPQRSTUVWXYZABC') == 'HELLO MAJOR GILBERT', decrypt_wbw('KHOOR QHOGU PQKLIHW', 'DEFGHIJKLMNOPQRSTUVWXYZABC'))
#print(decrypt_wbw('Y EBAJ XPHEOK', 'DQOLVJSGYCREUTBKXIWNHAMZPF') == 'I LOVE PYTHON', decrypt_wbw('Y EBAJ XPHEOK', 'DQOLVJSGYCREUTBKXIWNHAMZPF'))


################################################################
#                           TOPIC 2                            #
################################################################

from runes import *

## Question 4 ##

def stackn_list(pics):
    """ (List[Rune]) -> Rune

    Returns a stack of runes based on the input list pics.
    The 1st element of pics will be the top rune in the stack
    """
    if len(pics) == 1:
        return pics[0]
    else:
        return stack_frac(1/len(pics), \
                          pics[0],
                          stackn_list(pics[1:]))
    

#print("\n*** Question 4 ***")
#print(" --- need to visually check whether the rune is correct or not ---")
#show(stackn_list([make_cross(nova_bb), make_cross(rcross_bb), circle_bb, heart_bb]))
# show(stackn_list([make_cross(rcross_bb), make_cross(nova_bb), pentagram_bb, make_cross(nova_bb), make_cross(rcross_bb)]))


## Question 5 ##

def mxn_matrix(pics, matrix):
    """ (List[Rune], List[List[int]]) -> Rune

    Returns a rune composed of runes from pics.
    The position of a rune in the output rune is
    determined by:
    a. the index of the rune in pics
    b. the distribution of said index in the index matrix
    """
    row_pics = list(map(lambda i: quarter_turn_right(pics[i]), matrix[0]))
    # print(row_pics)
    if len(matrix) == 1:
        return quarter_turn_left(stackn_list(row_pics))
    else:
        return stack_frac(1/(len(matrix)), \
                          quarter_turn_left(stackn_list(row_pics)), \
                          mxn_matrix(pics, matrix[1:]))

#print("\n*** Question 5 ***")
#print(" --- need to visually check whether the rune is correct or not ---")
#show(mxn_matrix([make_cross(nova_bb), make_cross(rcross_bb), circle_bb, heart_bb], [[0, 1, 2, 3], [1, 0, 1, 2], [2, 1, 0, 1], [3, 2, 1, 0]]))
#show(mxn_matrix([make_cross(rcross_bb), make_cross(nova_bb), pentagram_bb], [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 2, 2, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]))


################################################################
#                           TOPIC 3                            #
################################################################

## Question 6 ##

def get_shape(arr):
    """ (Nested lists of ints) -> List[int]

    Returns a list of numbers where result[n] displays
    the number of elements in the n+1th dimension
    """
    if isinstance(arr[0], int):
        return [len(arr)]
    else:
        return [len(arr)] + get_shape(arr[0])
        

# print("\n*** Question 6 ***")
# print(get_shape([1]) == [1], get_shape([1]))
# print(get_shape([1, 2]) == [2], get_shape([1, 2]))
# print(get_shape([[1, 2, 3], [4, 5, 6]]) == [2, 3], get_shape([[1, 2, 3], [4, 5, 6]]))
# print(get_shape([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [2, 3, 2], get_shape([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))
# print(get_shape([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]) == [1, 2, 3, 2], get_shape([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]))


## Question 7 ##

def get_value(arr, idx):
    if len(idx) == 1:
         return arr[idx[0]]
    else:
         return get_value(arr[idx[0]], idx[1:])

# print("\n*** Question 7 ***")
# print(get_value([1], [0]) == 1, get_value([1], [0]))
# print(get_value([1, 2], [1]) == 2, get_value([1, 2], [1]))
# print(get_value([[1, 2, 3], [4, 5, 6]], [0, 2]) == 3, get_value([[1, 2, 3], [4, 5, 6]], [0, 2]))
# print(get_value([[1, 2, 3], [4, 5, 6]], [1, 1]) == 5, get_value([[1, 2, 3], [4, 5, 6]], [1, 1]))
# print(get_value([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]], [1, 0, 1]) == 8, get_value([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]], [1, 0, 1]))
# print(get_value([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]], [0, 1, 0, 1]) == 8, get_value([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]], [0, 1, 0, 1]))


## Question 8 ##

def set_value(arr, idx, val):
    if len(idx) == 1:
        arr[idx[0]] = val
    else:
        return set_value(arr[idx[0]], idx[1:], val)

# print("\n*** Question 8 ***")

# arr1 = [1]
# arr2 = [1, 2]
# arr3 = [[1, 2, 3], [4, 5, 6]]

# set_value(arr1, [0], 8)
# print(arr1 == [8], arr1)

# set_value(arr2, [1], 18)
# print(arr2 == [1, 18], arr2)

# set_value(arr3, [0, 2], 28)
# print(arr3 == [[1, 2, 28], [4, 5, 6]], arr3)


## Question 9 ##

def create_arr(shape):
    if len(shape) == 1:
        return [0] * shape[0]
    else:
        return [create_arr(shape[1:]).copy() for i in range(shape[0])]

# print("\n*** Question 9 ***")
# print(create_arr([2, 3]) == [[0, 0, 0], [0, 0, 0]], create_arr([2, 3]))
# print(create_arr([2, 3, 2]) == [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]], create_arr([2, 3, 2]))


## Question 10 ##
from time import sleep

def next_idx(idx, shape):
    if list(map(lambda x: x-1, shape)) == idx:
        return None
    for i in range(len(idx)-1, -1, -1):
        if idx[i] == shape[i]-1:
            idx[i] = 0
            continue
        elif idx[i] < shape[i]-1:
            idx[i] += 1
            return idx


def listing_of_indices_given_a_shape(shape):
	idx = [0] * len(shape)
	print(idx)
	while idx != None:
		idx = next_idx(idx, shape) # you are to implement this function
		print(idx)

# print("\n*** Question 10 ***")
# listing_of_indices_given_a_shape([5])           # output should be: [0] [1] [2] [3] [4] None
# listing_of_indices_given_a_shape([2, 3])        # [0, 0] [0, 1] [0, 2] [1, 0] [1, 1] [1, 2] None
# listing_of_indices_given_a_shape([4, 2, 2])     # [0, 0, 0] [0, 0, 1] [0, 1, 0] [0, 1, 1]
#                                                 # [1, 0, 0] [1, 0, 1] [1, 1, 0] [1, 1, 1]
#                                                 # [2, 0, 0] [2, 0, 1] [2, 1, 0] [2, 1, 1]
#                                                 # [3, 0, 0] [3, 0, 1] [3, 1, 0] [3, 1, 1] None
# listing_of_indices_given_a_shape([1, 2, 3, 2])  # output is as shown in the question paper


## Question 11 ##

def sum_along(axis, arr):
    """ Returns a single value as discussed when arr is 1D,
    or returns an output array of 1 less dimension as
    arr with sums along the given axis.
    """
    # Find the shape of the input array
    inp_shape = get_shape(arr)
    # print(f"inp_shape: {inp_shape}")

    # create the output array (of shape with 1 less dimension) 
    # with all initial values equal to 0.
    if len(inp_shape) == 1:
        output_arr = sum(arr)
    else:
        inp_shape.pop(axis)
        output_arr = create_arr(inp_shape)

    # Then go through each of the necessary index (using next idx) to 
    # sum up the values of those required elements (of the input array)
    # to be the value of the element of the output array with this index

    idx = [0] * len(inp_shape)

    while idx != None:
        if axis == 0:
            val = ...
            set_value(arr, idx, val)
        idx = next_idx(idx, inp_shape)

    # [[row[i] for row in arr] for i in range(len(arr[0]))]
    return output_arr


print("\n*** Question 11 ***")
print(sum_along(0, [1, 2]) == 3, sum_along(0, [1, 2]))

print(sum_along(0, [[1, 2, 3], [4, 5, 6]]) == [5, 7, 9], \
     sum_along(0, [[1, 2, 3], [4, 5, 6]]))

print(sum_along(1, [[1, 2, 3], [4, 5, 6]]) == [6, 15], \
     sum_along(1, [[1, 2, 3], [4, 5, 6]]))

print(sum_along(0, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [[8, 10], [12, 14], [16, 18]], \
     sum_along(0, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))

print(sum_along(2, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [[3, 7, 11], [15, 19, 23]], \
     sum_along(2, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))

print(sum_along(3, [[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]) == [[[3, 7, 11], [15, 19, 23]]], \
     sum_along(3, [[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]))


################################################################
#                           TOPIC 4                            #
################################################################

## Question 12 ##

class Matrix(object):
    ## Task A ###
    def __init__(self, nrows, ncols):
        """ self.matrix will only store non-zero values
        """
        self.matrix = {}
        self.nrows = nrows
        self.ncols = ncols

    def get(self, idx):
        try:
            return self.matrix[idx]
        except KeyError:
            row_num = idx[0]
            col_num = idx[1]
            if (0 <= row_num <= self.nrows) or (0 <= col_num <= self.ncols):
                return 0

    def insert(self, idx, val):
        self.matrix[idx] = val
        
    def delete(self, idx):
        self.matrix.pop(idx)
        
    def dict2list(self):
        """ Converts the dictionary representation here
        to a usual matrix represented as a list (that
        explicitly representing all the elements
        in the matrix inclusive of any zero).
        """
        result = create_arr([self.nrows, self.ncols])
        for key, val in self.matrix.items():
            set_value(result, key, val)
        return result


    ## Task B ###
    def transpose(self):
        """ (None) -> Matrix

        Transposes the matrix instance.
        The original matrix should NOT be changed
        """
        # To print a transposed list without changing self.matrix:
        # result = create_arr([self.ncols, self.nrows])
        # for key, val in self.matrix.items():
        #     set_value(result, sorted(key, reverse=True), val)
        # return result
        transposed = Matrix(self.ncols, self.nrows)
        for key, val in self.matrix.items():
            new_key = tuple(sorted(key, reverse=True))
            transposed.insert(new_key, val)
        return transposed


    ## Task C ###
    def multiply(self, m2):
        """ (Matrix) -> Matrix
        """
        res = [[0] * len(m1) for i in range(len(m2[0]))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                val = 0
                for k in range(len(m1[0])):
                    val += m1[i][k] * m2[k][j]
                res[i][j] = val

        return res

print("\n*** Question 12 ***")

print("\n** Task A **")
print("* Public Test 1 *")
m1 = Matrix(1, 3)
m1.insert((0,0), 1)
m1.insert((0,1), 2)
m1.insert((0,2), 3)
print(m1.dict2list() == [[1, 2, 3]], m1.dict2list())

print("* Public Test 2 *")
m1.delete((0,1))
print(m1.dict2list() == [[1, 0, 3]], m1.dict2list())

print("* Public Test 3 *")
print([m1.get((0,1)), m1.get((0,2)), m1.get((0,0))] == [0, 3, 1], [m1.get((0,1)), m1.get((0,2)), m1.get((0,0))])

print("\n** Task B **")
print("* Public Test 4 *")
m2 = m1.transpose()
print(m2.dict2list() == [[1], [0], [3]], m2.dict2list())

print("\n** Task C **")
print("* Public Test 5 *")
m3 = Matrix(1, 4)
m3.insert((0,0), 3)
m3.insert((0,1), 4)
m3.insert((0,3), 5)
m4 = m2.multiply(m3)
print(f"m2: {m2.dict2list()}")
print(f"m3: {m3.dict2list()}")
print(m4.dict2list() == [[3, 4, 0, 5], [0, 0, 0, 0], [9, 12, 0, 15]], m4.dict2list())

