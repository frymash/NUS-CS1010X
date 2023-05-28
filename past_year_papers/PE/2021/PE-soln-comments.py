############################################################
#
# Question 1
#
#############################################################
def day_of_date( dd, mm, yyyy ):
    ## dictionary is not good in most parts for this question
    ##
    ## style is -0.5 for wrongly use dictionary at each box. 
    ## not good naming of variables may lose credit at time too.
    ## max of deduction from style is 1. 
    ## correctness is -1 for wrongly "calculate" at each box
    ## the index is the key to retrieve the values saved in tuple
    nonLeap = (0,3,3,6,1,4,6,2,5,0,3,5)
    leap    = (6,2,3,6,1,4,6,2,5,0,3,5)
    century = {16:0, 17:6, 18:4, 19:2, 20:0, 21:6}  # dictionay is allowed for this one though still could be avoided
    date = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    
    box1 = dd
    box2 = leap[mm-1] if yyyy % 400 == 0 or (yyyy % 4 == 0 and yyyy % 100 != 0) else nonLeap[mm-1]
    box3 = century[yyyy//100 + 1] # yyyy//100 + 1 gives the century 
    box4 = yyyy % 100             # yyyy%100 gives the first 2 digits for our range of year
    box5 = box4 // 4
    total = box1 + box2 + box3 + box4 + box5
    return date[total%7]

############################################################
#
# Question 2
#
#############################################################

#### A ########
def stackn_alt(n, pic1, pic2):
    ## Four evaluation test cases, one mark each.
    ## For two of them, n is odd, and for the other two, n is even.
    ## For two of them, pic1 and pic2 are centrosymmetric, for the other two, they are not.
    ## In general, no mark if your code has syntax error.
    if n == 1:
        return pic1
    else:
        return stack_frac(1/n, pic1, stackn_alt(n-1, pic2, pic1))

#### B ########
def nxn_alt(n, pic1, pic2):
    ## Four evaluation test cases, one mark each.
    ## For two of them, n is odd, and for the other two, n is even.
    ## For two of them, pic1 and pic2 are centrosymmetric, for the other two, they are not.
    ## -1 if your code is not written in one line.
    ## In general, no mark if your code has syntax error.
    return stackn_alt(n, quarter_turn_left(stackn_alt(n, quarter_turn_right(pic1), quarter_turn_right(pic2))),
                         quarter_turn_left(stackn_alt(n, quarter_turn_right(pic2), quarter_turn_right(pic1))))

#### C ########
def nxn_alt(n,pic1, pic2):
    ## Four evaluation test cases, one mark each.
    ## For two of them, n is odd, and for the other two, n is even.
    ## For two of them, pic1 and pic2 are centrosymmetric, for the other two, they are not.
    ## No mark if you put a recursive solution here.
    ## In general, no mark if your code has syntax error.
    stack_pic = [quarter_turn_left(stackn_alt(n, quarter_turn_right(pic1), quarter_turn_right(pic2))),
                quarter_turn_left(stackn_alt(n, quarter_turn_right(pic2), quarter_turn_right(pic1)))]
    previous = stack_pic[0]
    for i in range(1, n):
        previous = stack_frac(i/(i+1), previous, stack_pic[i%2])
    return previous

############################################################
#
# Question 3
#
#############################################################

#### A ########
# O(n²m²)
## No mark if the answer is not correct.

#### B ########
def better_sum(lst):
    ## Six evaluation test cases, 0.5 each.
    ## -1 if you calculate the prefix sum using the build-in sum() function.
    ## -1 if you calculate the prefix sum using high order functions, and creating new lists in each step.
    ## -0.5 if you modified the original lst.
    ## In general, no mark if your code has syntax error.
    result = [[lst[i][j] for j in range(len(lst[0]))] for i in range(len(lst))]
    # horizontal prefix sum
    for i in range(len(result)):
        for j in range(1, len(result[0])):
            result[i][j] += result[i][j-1]
    # vertical prefix sum
    for j in range(len(result[0])):
        for i in range(1, len(result)):
            result[i][j] += result[i-1][j]
    return result

#### C ########
def dp_sum(lst):
    ## Six evaluation test cases, 0.5 each.
    ## -0.5 if you modified the original lst.
    ## +0.5 ~ 1.0, if you failed the test cases but is close to the correct answer, depending on the circumstances.
    ## No mark if your solution is the horizontal-vertical prefix sum version.
    ## No mark if you simply copy the answer from better_sum.
    ## No mark for naive solutions.
    ## In general, no mark if your code has syntax error.
    result = [[lst[i][j] for j in range(len(lst[0]))] for i in range(len(lst))]
    # prefix sum of the first column
    for i in range(1, len(result)):
        result[i][0] += result[i-1][0]
    # prefix sum of the first row
    for j in range(1, len(result[0])):
        result[0][j] += result[0][j-1]
    # dp solution
    for i in range(1, len(result)):
        for j in range(1, len(result[0])):
            result[i][j] = result[i][j] + result[i][j-1] + result[i-1][j] - result[i-1][j-1]
    return result

#### D ########
# Both solutions take O(nm) time. There's no difference in terms of time complexity.
## No mark if the time complexity is not correct.
## 0.5 if the time complexity is correct, but said that dp_sum or better_sum is better in terms of time complexity.

#### E ########
def search_rect_sum(result_lst, ii, jj, i, j):
    ## Nine test cases (including the public test cases), one mark for each 3 test cases.
    ## +1.0 ~ 1.5, if you failed some test cases but can understand the algorithm, depending on the circumstances.
    ## No mark for naive solutions (using for-loops, returning result_lst[i-ii][j-jj], etc.).
    ## In general, no mark if your code has syntax error.
    if ii == 0 and jj == 0:
        return result_lst[i][j]
    elif ii == 0:
        return result_lst[i][j] - result_lst[i][jj - 1]
    elif jj == 0:
        return result_lst[i][j] - result_lst[ii - 1][j]
    else:
        return result_lst[i][j] - result_lst[ii - 1][j] - result_lst[i][jj - 1] + result_lst[ii - 1][jj - 1]
