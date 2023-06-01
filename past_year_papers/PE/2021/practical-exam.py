############################################################
#
# Question 1
#
#############################################################
def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def day_of_date(dd, mm, yyyy):
    box2_nonleap = (0,3,3,6,1,4,6,2,5,0,3,5)
    box2_leap = (6,2,3,6,1,4,6,2,5,0,3,5)
    box3_map = {"15":0, "16":6, "17":4, "18":2, "19":0, "20":6}
    result_mappings = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", \
                    4:"Thursday", 5:"Friday", 6:"Saturday"}
    
    box1 = dd
    
    month_index = mm - 1
    if not is_leap_year(yyyy):
        box2 = box2_nonleap[month_index]
    else:
        box2 = box2_leap[month_index]

    box3 = box3_map[str(yyyy)[:2]]
    box4 = int(str(yyyy)[2:])
    box5 = box4 // 4
    box_sum = box1 + box2 + box3 + box4 + box5
    return result_mappings[box_sum % 7]


print ("")
print (" * * * Question 1 * * *")
print (day_of_date(25, 12, 2000) == "Monday")
print (day_of_date(25, 12, 1900) == "Tuesday")
print (day_of_date(1, 1, 1997) == "Wednesday")
print (day_of_date(11, 11, 1999) == "Thursday")
print (day_of_date(1, 1, 1897) == "Friday")
print (day_of_date(5, 6, 2021) == "Saturday")
print (day_of_date(5, 6, 1898) == "Sunday")

############################################################
#
# Question 2
#
#############################################################
from runes import *

def stackn(n,pic):
    if n == 1: 
        return pic
    else: 
        return stack_frac(1/n, pic, stackn(n-1, pic))

def nxn(n,pic):
    return stackn(n, quarter_turn_right(stackn(n, quarter_turn_left(pic) ) ) )

print ("")
print (" * * * Question 2 * * *")
#########
#
# Question 2: Question 2 A.
#
#########
def stackn_alt(n, pic1, pic2):
    if n == 1:
        return pic1
    elif n == 2:
        return stack_frac(1/2, pic1, pic2)
    else:
        return stack_frac(1/n, pic1, stackn_alt(n-1, pic2, pic1))

#show(stack_frac(1/2, rcross_bb, nova_bb))
#show(stackn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(stackn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
#show(stackn_alt(5, make_cross(circle_bb), make_cross(heart_bb)))

#########
#
# Question 3: Question 2 B. 
# Recursive
#
#########
def nxn_alt(n, pic1, pic2):
    return stackn_alt(n, \
                      quarter_turn_left(stackn_alt(n, \
                                                    quarter_turn_right(pic1), \
                                                    quarter_turn_right(pic2))), \
                      quarter_turn_left(stackn_alt(n, \
                                                    quarter_turn_right(pic2), \
                                                    quarter_turn_right(pic1))))

    
#show(nxn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(4, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(5, make_cross(circle_bb), make_cross(heart_bb)))

#########
#
# Question 4: Question 2 C. 
# Use for or while loop
#
#########
def nxn_alt(n, pic1, pic2):
    result = quarter_turn_right(stackn_alt(n, \
                                          quarter_turn_left(pic1), \
                                          quarter_turn_left(pic2)))
    for i in range(2, n+1):
        pic1, pic2 = pic2, pic1
        to_add = quarter_turn_right(stackn_alt(n, \
                                              quarter_turn_left(pic1), \
                                              quarter_turn_left(pic2)))
        result = stack_frac(1/i, to_add, result)
    return result
#show(nxn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(4, make_cross(nova_bb), make_cross(rcross_bb)))
show(nxn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(5, make_cross(circle_bb), make_cross(heart_bb)))


############################################################
#
# Question 3
#
#############################################################
lst = [ [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 0, 1, 2, 3, 4, 5, 6],
        [7, 8, 9, 0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9, 0, 1, 2],
        [3, 4, 5, 6, 7, 8, 9, 0] ]

lst2 = [[-2, 94, 7, -90, -34],
        [30, 24, 3, 100, -23],
        [22, -9, 49, -45, 29], 
        [-65, -28, -65, 93, -76], 
        [58, -36, 36, 80, 54]]

lst3 = [[-66, 45, 95, -84, -35, -70, 26, 94, 15, 20],
        [66, -3, -47, -76, 24, -93, -1, 10, 55, 95], 
        [96, -100, 78, 14, -32, 84, -42, 51, -74, -19], 
        [-93, -95, -94, 66, 38, -98, -3, 75, -45, 8], 
        [85, -93, 35, -44, 95, 12, 26, 41, -41, -12]]

lst4 = [[-86, -77, -79, -8, -57],
        [88, 71, -22, -36, 55],
        [-46, 55, -91, 48, 74],
        [-60, 10, 63, 0, 85],
        [30, -5, 39, 13, 28],
        [-32, -91, -93, -7, 19],
        [-19, -3, 8, 34, -58],
        [43, -55, -40, -41, -94],
        [-55, -17, -56, -66, 30],
        [30, -8, 31, 72, 43]]


def rect_sum(lst, i, j):
    sum = 0
    for ii in range(0, i+1):
        for jj in range(0, j+1):
            sum += lst[ii][jj]
    return sum

def naive_sum(lst):
    result_lst = []
    for i in range(0, len(lst)):
        result_lst.append([0]*len(lst[0]))
        for j in range(0, len(lst[0])):
            result_lst[i][j] = rect_sum(lst, i, j)
    return result_lst

sample_result = naive_sum(lst)
sample_result2 = naive_sum(lst2)
sample_result3 = naive_sum(lst3)
sample_result4 = naive_sum(lst4)

#########
#
# Question 5: Question 3 A.
#
#########
# State the time complexity in coursemology
# 3(a): O(n^2 m^2)

#########
#
# Question 6: Question 3 B.
#
#########

# Time complexity: O(n*m)
def hori_prefix_sum(lst):
    result = []
    for i in range(len(lst)):
        row = [lst[i][0]]
        for j in range(1, len(lst[0])):
            row.append(lst[i][j] + row[j-1])
        result.append(row)
    return result

# Time complexity: O(n*m)
def better_sum(lst):
    result_lst = []
    horizontal_lst = hori_prefix_sum(lst)

    for i in range(len(lst)):
        result_lst.append([0]*len(lst[0]))
        for j in range(len(lst[0])):
            if i == 0:
                result_lst[i][j] = horizontal_lst[i][j]
            else:
                result_lst[i][j] = horizontal_lst[i][j] + result_lst[i-1][j]
    return result_lst

print ("")
print (" * * * Question 3B * * *")
print( sample_result == better_sum(lst) )
print( sample_result2 == better_sum(lst2) )
print( sample_result3 == better_sum(lst3) )
print( sample_result4 == better_sum(lst4) )

#########
#
# Question 7: Question 3 C.
#
#########
def dp_sum(lst):
    # Initialize table
    m = len(lst)
    n = len(lst[0])
    single_row = [0]*n
    result_lst = []
    for _ in range(m):
        result_lst.append(single_row.copy())

    # Set up first row and first column of table
    first_row = lst[0]
    first_col = [lst[i][0] for i in range(m)]
    # print(f"first_row: {first_row}")
    # print(f"first_col: {first_col}")
    result_first_row = hori_prefix_sum([first_row])
    result_first_col = hori_prefix_sum([first_col])
    result_lst[0] = result_first_row[0]
    for k in range(1, m):
        result_lst[k][0] = result_first_col[0][k]

    # print("Table after initial setup:")
    # for row in result_lst:
    #     print(row)

    # Set up remainder of table
    for i in range(1,m):
        for j in range(1,n):
            result_lst[i][j] = lst[i][j] \
                               + result_lst[i-1][j] \
                               + result_lst[i][j-1] \
                               - result_lst[i-1][j-1]
    
    return result_lst

# print(f"dp_sum(lst):")
# for row in dp_sum(lst):
#     print(row)

print ("")
print (" * * * Question 3C * * *")
print( sample_result == dp_sum(lst) )
print( sample_result2 == dp_sum(lst2) )
print( sample_result3 == dp_sum(lst3) )
print( sample_result4 == dp_sum(lst4) )

#########
#
# Question 8: Question 3 D.
#
#########
# State the time complexity in coursemology
# There is no difference in time complexity; both implementations
# have a time complexity of O(m*n).

#########
#
# Question 9: Question 3 E.
#
#########
def search_rect_sum(result_lst, ii, jj, i, j):
    if ii == 0 and jj == 0:
        return result_lst[i][j]
    elif ii == 0:
        return result_lst[i][j] \
                - result_lst[i][jj-1]
    elif jj == 0:
        return result_lst[i][j] \
                - result_lst[ii-1][j]
    else:
        return result_lst[i][j] \
               - result_lst[ii-1][j] \
               - result_lst[i][jj-1] \
               + result_lst[ii-1][jj-1]

print ("")
print (" * * * Question 3E * * *")
x = sample_result
print( search_rect_sum(x, 0, 0, 4,7) == 180 )
print( search_rect_sum(x, 3, 6, 4,7) == 12 )
print( search_rect_sum(x, 3, 7, 4,7) == 2)
print( search_rect_sum(x, 4, 6, 4,7) == 9)
print( search_rect_sum(x, 1, 0, 4, 7) == 144)
print( search_rect_sum(x, 1, 0, 3, 6) == 90)
print( search_rect_sum(x, 0, 1, 3, 6) == 96)
print( search_rect_sum(x, 1, 1, 3, 6) == 69)
print( search_rect_sum(x, 2, 3, 3, 6) == 24)

print( search_rect_sum(sample_result2, 0, 0, 4, 4) == 206 )
print( search_rect_sum(sample_result3, 2, 3, 4, 9) == 100 )
print( search_rect_sum(sample_result4, 3, 2, 9, 4) == 10 )
