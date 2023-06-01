# Question 3

def is_leap_year(year):
    # DONE: do not need to modify
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False

def is_valid(d, m, y):
    # DONE: do not need to modify    
    # d, m, y represents day, month, and year in integer.
    if y < 1970 or y > 9999:
        return False
    if m <= 0 or m > 12:
        return False
    if d <= 0 or d > 31:
        return False

    if m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            return False

    if is_leap_year(y):
        if m == 2 and d > 29:
            return False
    else:
        if m == 2 and d > 28:
            return False
        
    return True

def get_day_month_year(date):
    # TODO: split the date and return a tuple of integer (day, month, year)
    d,m,y = map(int, date.split("/"))
    return (d, m, y)

def less_than_equal(start_day, start_mon, start_year, \
                    end_day, end_mon, end_year):    
    # TODO: return true if start date is before or same as end date
    return (start_year, start_mon, start_day) <= (end_year, end_mon, end_day)

def next_date(d, m, y):
    # TODO: get the next date from the current date (d, m, y)
    # return a tuple of integer (day, month, year).
    max_days = {28: (2,), 30: (4,6,9,11), 31: (1,3,5,7,8,10)}
    if d == 31 and m == 12:
        return (1,1, y+1)
    elif d == 29 and m == 2:
        return (1,3, y)
    elif d in max_days:
        if m == 2 and is_leap_year(y):
            return (29, 2, y)
        elif m in max_days[d]:
            return (1, m+1, y)
    return (d+1, m, y)

def days_since_year_start(date_tup):
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31,\
                     6:30, 7:31, 8:31, 9:30, 10:31, \
                     11:30, 12:31}
    count = 0
    day, month, _ = date_tup
    for i in range(1, month):
        count += days_in_month[i]
    count += day
    return count - 1

def count_days(start_date, end_date):    
    # date is represented as a string in format dd/mm/yyyy
    start_date_tup = get_day_month_year(start_date)
    start_day, start_mon, start_year = start_date_tup
    end_date_tup = get_day_month_year(end_date)
    end_day, end_mon, end_year = end_date_tup

    # TODO: check for data validity here #
    print(f"start_date: {start_date_tup}")
    print(f"end_date: {end_date_tup}")
    if not is_valid(*start_date_tup):
        raise Exception("Not a valid date: " + start_date)
    elif not is_valid(*end_date_tup):
        raise Exception("Not a valid date: " + end_date)
    elif not less_than_equal(*start_date_tup, *end_date_tup):
        raise Exception("Start date must be less than or equal end date.")
    
    else:
        # lazy - let the computer count from start date to end date
        count = 0
        
        for year in range(start_year, end_year+1):
            if is_leap_year(year):
                count += 366
            else:
                count += 365
        count -= days_since_year_start(start_date_tup)
        count -= (365 - days_since_year_start(end_date_tup))
        return count


# Question 4

def pascal(row, col):
    if col == 1 or col == row:
        return 1
    else:
        return pascal(row - 1, col) + pascal(row - 1, col - 1)
    

def faster_pascal(row_len, col_len):
    row = [0] * (col_len)
    table = []

    # Create table
    for i in range(row_len):
        table.append(row.copy())

    # Change the 1st element in every row to 1
    for row in table:
        row[0] = 1

    # Enumerate table
    for row in range(1, row_len):
        for col in range(1, col_len):
            table[row][col] = table[row-1][col-1] + table[row-1][col]

    # for row in table:
    #     print(row)
    
    return table[row_len-1][col_len-1]


# Question 5

memoize_table = {}

def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name] = {}
    table = memoize_table[name]
    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args)
            table[args] = result
            return result
    return helper

def num_of_paths(n, m):
    def helper(n, m):
        if n == 1 and m == 1:
            return 0
        elif n == 1 or m == 1:
            return 1
        else:
            return num_of_paths(n-1, m) + num_of_paths(n, m-1)
    return memoize(helper, "num_of_paths")(n,m)


# Question 7

def num_of_paths_maze(maze):
    # Initialize an empty table (dictionary), get number of rows n and number of columns m
    table = {}
    n = len(maze)
    m = len(maze[0])
    # print(f"n: {n}, m: {m}")
    
    # Fill in the first row. For j in range m:
    for j in range(m):
        # If maze[0][j] is safe, set table[(0, j)] to be 1 because there's one way to go there.
        if maze[0][j] == 1:
            table[(0, j)] = 1
        # If maze[0][j] has a bomb, set table[(0, k)] where k >= j to be 0. Since one cell is broken along the way, all following cells cannot be reached.
        elif maze[0][j] == 0:
            for k in range(j, m):
                table[(0, k)] = 0
            break
        else:
            raise ValueError(f"Row 1, column {j} contains a value that is not 0 or 1.")
        
    # Fill in first column. For i in range n:
    for i in range(n):
        # If maze[i][0] is safe, set table[(i, 0)] to be 1 because there's one way to go there.
        if maze[i][0] == 1:
            table[(i, 0)] = 1
        # If maze[i][0] has a bomb, set table[(i, 0)] and all cells under it to be 0. The reason is same as row.
        elif maze[i][0] == 0:
            for r in range(i, n):
                table[(r, 0)] = 0
            break
        else:
            raise ValueError(f"Row {i}, column 1 contains a value that is not 0 or 1.")

    # print(f"Pre-DP table: {table}")
    
    # Main DP procedure - fill in the rest of the table. If maze[i][j] has a bomb, set table[(i, j)] = 0. Otherwise, table[(i, j)] = table[(i - 1, j)] + table[(i, j - 1)]
    for i in range(1, n):
        for j in range(1, m):
            # print(i,j)
            if maze[i][j] == 0:
                table[(i,j)] = 0
            else:
                table[(i,j)] = table[(i-1, j)] + table[(i, j-1)]

    # print(table)

    #  Return table[(n - 1, m - 1)]
    return table[(n-1, m-1)]

# Do NOT modify

maze1 = ((1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
         (1, 0, 0, 1, 1, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
         (1, 1, 0, 1, 1, 1, 1, 0, 1, 1),
         (0, 1, 0, 1, 0, 0, 1, 0, 1, 0),
         (1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
         (1, 1, 0, 1, 0, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
         (1, 0, 1, 0, 0, 1, 1, 0, 1, 1),
         (1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
         (1, 1, 0, 1, 0, 1, 0, 1, 1, 1))


maze2 = ((1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1))


maze3 = ((1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 0),
         (1, 0, 0, 1))

num_of_paths_maze(maze1)
num_of_paths_maze(maze2)
num_of_paths_maze(maze3)
