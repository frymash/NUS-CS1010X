# 5 things u can do with a collection
# 1. map
# 2. filter
# 3. accumulate
# 4. sort
# 5. searching

# Q1(c)

def at_least_n(lst,n):
    i = 0
    while i < len(lst):
        if lst[i] < n:
            lst.pop(i)
        else:
            i += 1
    return lst

def at_least_n(lst, n):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] < n:
            lst.pop(i)
    return lst


# Q1(d)

def at_least_n(lst, n):
    return list(filter(lambda x: x >= n, lst))

# Trivia from 2030S: Generator objects (such as a filter object) are lazily evaluated.
# We need to call list on it in order to evaluate the object.

# Q2(c)

def col_sum(matrix):
    return list(sum(map(lambda row: row[i], matrix)) for i in range(len(matrix[0])))


# Q2(d)

def row_sum(matrix):
    return list(map(sum, matrix))

# Q3

# Time complexity: O(n*m)
# Space complexity: O(n)

def transpose(matrix):
    temp = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if len(temp) <= j:
                temp.append([matrix[i][j]])
            else:
                temp[j].append(matrix[i][j])
    matrix.clear()
    matrix.extend(temp)
    return matrix

def transpose(matrix):
    temp = []
    for i in range(len(matrix[0])):
        temp.append(list(map(lambda row: row[i], matrix)))
    matrix.clear()
    matrix.extend(temp)
    return matrix

def transpose(matrix):
    temp = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    matrix.clear()
    matrix.extend(temp)
    return matrix

# Q4

# Cool trivia: you can clear a list m by writing m *= 0

# Insertion sort and bubble sort are O(n) in the best-case scenario (if the list is nearly sorted)
# Python's sort method uses the Timsort algo. It's a mix of multiple sorting algos.

# Timsort is "online", meaning that it can still sort a collection
# even if the elements are inserted one by one

# Can we do better than O(n log n) for sorting?
# Yes, counting sort runs in O(n + k) time and radix sort runs in O(n*k/d) time.
# Quicksort is the sorting algo that is used the most often.

# In-place algo -> an algo that uses O(1) auxiliary space
# (the extra space that is taken by an algorithm temporarily to finish its work).
# You can typically assume that auxiliary space is equivalent to space complexity.

# Is it possible for recursive sorting algos to run in-place?
# Technically yes.

# What does it mean for an algorithm to be stable?
# If there are duplicate elements, they will remain in the same order.

# Even though insertion, selection, and bubble sort all run in O(n^2) time,
# insertion sort typically performs better than selection and bubble sort on avg.
# Insertion sort runs in O(1/4 n^2) time (if we were to care about the constant multiplier)
# Selection and bubble sort run in approximately O(1/2 n^2)
# (since the number of steps would form an arithmetic series with terms
# n + (n-1) + (n-2) + ... + 1, the AP sum would be n(n-1)/2)