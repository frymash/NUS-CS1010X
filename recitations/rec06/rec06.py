from math import inf
# --- Question 1 ---

many_things = [1, 'a', ('I', 'can', 'have', 'tuples', 'in', 'lists')]
print(many_things) # [1, 'a', ('I', 'can', 'have', 'tuples', 'in', 'lists')]

numbers = [2, 3, 4]
print(numbers) # [2, 3, 4]

concatenated = many_things + numbers
print(concatenated) # [1, 'a', ('I', 'can', 'have', 'tuples', 'in', 'lists'), 2, 3, 4]

appended = many_things.append(numbers)
print(appended) # None
print(many_things) # [1, 'a', ('I', 'can', 'have', 'tuples', 'in', 'lists'), [2, 3, 4]]

extended = many_things.extend(numbers)
print(extended) # None
print(many_things) # [1, 'a', ('I', 'can', 'have', 'tuples', 'in', 'lists'), [2, 3, 4], 2, 3, 4]

many_things[0] = 7
print(many_things) # [7, 'a', ('I', 'can', 'have', 'tuples', 'in', 'lists'), [2, 3, 4], 2, 3, 4]

can_be_indexed = concatenated[2]
print(can_be_indexed) # ('I', 'can', 'have', 'tuples', 'in', 'lists')

can_be_indexed_multiple_times = concatenated[2][1]
print(can_be_indexed_multiple_times) # can (strings aren't accompanied with inverted commas when printed outside a container)

a_shallow_copy = concatenated[:]
print(a_shallow_copy) # [1, 'a', ('I', 'can', 'have', 'tuples', 'in', 'lists'), 2, 3, 4]
print(a_shallow_copy == concatenated) # True
print(a_shallow_copy is concatenated) # False (because concatenated[:] will return a new list with the same elements as concatenated)

woops = a_shallow_copy[2]
print(woops) # ('I', 'can', 'have', 'tuples', 'in', 'lists')
print(woops is can_be_indexed) # True (because woops and can_be_indexed point to the same tuple)

singleton = ['blah']
print(singleton) # ['blah']


# --- Question 2 ---
def bubble_sort(lst):
    """ The nth largest element of the list will always be sorted after the
    nth iteration of the list.

    Best case time complexity: O(n)
    Worst case time complexity: O(n^2)

    Space complexity is O(1) in any case since the sorting is done in-place.
    """
    for _ in range(len(lst)-1): # n-1 total comparisons for a list of length n
        for i in range(len(lst)-1):
            if lst[i+1] < lst[i]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
    return lst


# --- Question 3 ---
'''
def selection_sort(lst):
    """ In-place selection sort

    # Time: O(n^2)
    # Space: O(1)
    """
    smallest = inf
    smallest_index = None
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            # print(f"lst: {lst} | list to check: {lst[i:]} | i = {i} | smallest: {smallest} | smallest_index: {smallest_index}")
            if len(lst[i:]) > 0 and lst[j] < smallest:
                smallest = lst[j]
                smallest_index = j
        lst[i], lst[smallest_index] = lst[smallest_index], lst[i]
        smallest = inf
    return lst
'''

# Prof's version
def selection_sort(lst):
    if len(lst) < 2:
        return
    else:
        for j in range(len(lst)-1):
            min = j
            for i in range(j+1, len(lst)):
                if lst[min] > lst[i]:
                    min = i
            lst[j], lst[min] = lst[min], lst[j]
            # print(j, lst)
        return


lst = [5,7,4,9,8,5,6,3]
print(f"Bubble sort result: {bubble_sort(lst)}") # [3,4,5,5,6,7,8,9]

lst = [5,7,4,9,8,5,6,3]
print(f"Selection sort result: {selection_sort(lst)}") # [3,4,5,5,6,7,8,9]


# --- Question 4 ---

students = [
('tiffany', 'A', 15),
('jane', 'B', 10),
('ben', 'C', 8),
('simon', 'A', 21),
('john', 'A', 15),
('jimmy', 'F', 1),
('charles', 'C', 9),
('freddy', 'D', 4),
('dave', 'B', 12 )]

# (a)
a = sorted(students, reverse=True)
print(a)

# (b). Names must be sorted first before grades
# b = sorted(students)
# b = sorted(b, key=lambda student: student[1])
# print(b)
b = sorted(students, key=lambda student: (student[1], student[0]))

# (c)
def names_under_six(students):
    filter_by_name = filter(lambda student: len(student[0]) < 6, students)
    isolate_name = map(lambda student: student[0], filter_by_name)
    return tuple(isolate_name)

print(names_under_six(students))

# (d)
def grades_and_occurrences(students):
    grades = tuple(map(lambda student: student[1], students))
    print(grades)
    grade_set = ()
    result = []
    for grade in grades:
        if grade not in grade_set:
            result += ((grade, 1),)
            grade_set += (grade,)
        else:
            print(result)
            for i in range(len(students)):
                if result[i][0] == grade:
                    result[i] = (result[i][0], result[i][1] + 1)
        print(grade_set)
    return result
"""
# Dictionary implementation:

def grades_and_occurrences(students):
    grades = tuple(map(lambda student: student[1], students))
    print(f"Grades: {grades}")
    result = {}
    for grade in grades:
        if grade not in result:
            result[grade] = 1
        else:
            result[grade] += 1
    return result
"""
    
print(grades_and_occurrences(students))

# Supplementary: deep copy
# list.copy() copies a list at a "shallow" level
# i.e. the memory references for any nested lists from the original
# list will be carried over to the copied list.
def deepcopy(lst):
    result = []
    for element in lst:
        if type(element) == list:
            result.append(deepcopy(element))
        else:
            result.append(element)
    return result
