# --- Question 1 ---

def make_matrix1(seq):
    mat = []
    for row in seq:
        mat.append(list(row))
    return mat

# 1(a)
def make_matrix(seq):
    return seq

"""
The implementation won't work since a matrix is represented
by nested lists in this question.

The value produced by make_matrix(seq) would be an alias of seq
although we would need it to produce a new object.
"""

# 1(b)
def rows(m):
    """ Returns the number of rows in matrix m

    Time: O(1) (len in Python is an O(1) operation)
    """
    return len(m)

def cols(m):
    """ Returns the number of columns in matrix m

    Time: O(1)

    Note: cols won't work if m is a null matrix.
    """
    return len(m[0])

def get(m,i,j):
    """ Returns the element (i,j) for matrix object m

    Time: O(1) (indexing is an O(1) time op)
    Space: O(1) (op doesn't use any space whatsoever)
    """
    return m[i][j]

def set_elt(mat, i, j, val):
    """ Sets the element (i,j) for matrix object m to value val
    """
    mat[i][j] = val

"""
def transpose(m):
    result = []
    curr_row = []
    for index in range(rows(m)):
        for row in m:
            curr_row.append(row[index])
        result.append(curr_row)
        curr_row = []
    return result
"""

"""
def transpose(m):
    result = []
    for i in range(cols(m)):
        result.append(list(map(lambda x: x[i]), m))
    m[:] = result
"""

"""
def sumT(t, term, next):
    if t == []:
        return []
    else:
        return term(t) + sumT(next(t), term, next)

def map(f,t):
    return sumT(t, lambda t: [f(t[0])], lambda t: t[1:])

def transpose(m):
    return sumT(t, lambda N: [map(lambda row: row[0], N)],
                lambda N: map(lambda row: row[1:], N) if len(N[0]) > 1 else [])
"""


def transpose(m):
    transposed = []
    for i in range(cols(m)):
        column = []
        for j in range(rows(m)):
            column.append(get(m,j,i))
        transposed.append(column)
    # m = transposed
    # m.clear()
    # m.extend(transposed)
    m[:] = transposed

def print_matrix(mat):
    for row in mat:
        print(row)


# 2(a)
def make_matrix2(seq):
    data = []
    for i in range(len(seq)):
        for j in range(len(seq[0])):
            if seq[i][j] != 0:
                data.append([i,j,seq[i][j]])
    return [len(seq), len(seq[0]), data]

def rows2(m):
    """ Returns the number of rows in matrix m
    """
    return len(m[2])

def cols2(m):
    """ Returns the number of columns in matrix m
    """
    return len(m[2][0])

'''
def get2(m,i,j):
    """ Returns the element (i,j) for matrix object m
    """
    matrix = m[2]
    for row in matrix:
        # print(row)
        if row[0] == i and row[1] == j:
            return row
'''

def get2(m, x, y):
    """
    Time: O(n) where n is the size of m[2] (which is the number of non-zero
    entities in the matrix)
    """
    for x1, y1, val in m[2]:
        if x == x1 and y == y1:
            return val
'''
def set_elt2(mat, i, j, val):
    """ Sets the element (i,j) for matrix object m to value val
    """
    matrix = mat[2]
    for index in range(len(matrix)):
        if i == matrix[index][0] and j == matrix[index][1]:
            matrix[index] = [i,j,val]
            break
'''
def set_elt2(m, i, j, val):
    """ Take note: you must account for the removal
    of zero values in the sparse matrix.

    Time: O(n) where n is the size of m[2] (which is the number of non-zero
    entities in the matrix)
    """
    for record in m[2]:
        if i == record[0] and j == record[1]:
            if val != 0:
                record[2] = val
            else:
                m[2].remove(record)
            return
    if val != 0:
        m[2].append([i,j,val])

def transpose2(m):
    matrix = m[2]
    # print_matrix(matrix)
    result = []
    curr_row = []
    for index in range(rows2(matrix)):
        for row in matrix:
            curr_row.append(row[index])
        result.append(curr_row)
        curr_row = []
    return [m[0], m[1], result]

"""
def transpose2(m):
    m[0], m[1] = m[1], m[0]
    for record in m[2]:
        record[0], record[1] = record[1], record[0]
"""

def print_matrix2(mat):
    for row in mat[2]:
        print(row)

# 2(b)
""" 
Depends on the situation/functions that must.

Sparse matrices are great when we're dealing with matrices that
have a lot of zero values.
"""

### Testing ###
m1 = make_matrix([[1,2,3],[4,5,6],[7,8,9]])
transpose(m1)
print_matrix(m1)
