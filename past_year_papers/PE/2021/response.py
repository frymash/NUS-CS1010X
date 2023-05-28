from icecream import ic

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

print("---- QUESTION 1 TESTS ----")
ic(day_of_date(5, 6, 2021) == "Saturday")
ic(day_of_date(25, 12, 2000) == "Monday")
ic(day_of_date(25, 12, 1900) == "Tuesday")
ic(day_of_date(1, 1, 1997) == "Wednesday")


# 3(a): O(n^2 m^2)

# 3(b)

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


# 3(c)
def dp_sum(lst):
    pass

# 3(d)
# Answer:

# 3(e)
