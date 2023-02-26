#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    state = get_table_state(table)
    first_coin = state[0]
    second_coin = state[1]
    if first_coin != second_coin:
        flip_coins(table, (1,0))

# test:
t2_1 = create_table(2)
solve_trivial_2(t2_1)
print(f"Task 1 solved: {check_solved(t2_1)}")


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

t2_1_run = create_table(2)
run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(2)
# Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    state = get_table_state(table)
    moveset = ()
    for coin in state:
        if coin == 0:
            moveset += (1,)
        else:
            moveset += (0,)
    flip_coins(table, moveset)
    
    

# test:
t4_2 = create_table(4)
solve_trivial_4(t4_2)
print(f"Task 2 solved: {check_solved(t4_2)}")


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

t4_2_run = create_table(4)
run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_2_susan = create_table(4)
# Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    solved = check_solved(table)
    if not solved:
        flip_coins(table, (1,0))

# test:
t2_3 = create_table(2)
solve_2(t2_3)
print(f"Task 3 solved: {check_solved(t2_3)}")


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

t2_3_run = create_table(2)
# run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    solved = check_solved(table)
    if not solved:
        A = (1,0,1,0)
        B = (1,1,0,0)
        C = (1,0,0,0)
        moveset = (A,B,A,C,A,B,A)
        for move in moveset:
            flip_coins(table, move)
            solved = check_solved(table)
            if solved:
                break

# test:
t4_4 = create_table(4)
solve_4(t4_4)
print(f"Task 4 solved: {check_solved(t4_4)}")


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

t4_4_run = create_table(4)
# run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def solve(table):
    def generate_moves_for_n_coins(n):
        """ Generates all possible moves for a table with n coins.
        """
        def moveset_generator(n):
            if n == 2:
                return ((1,1), (1,0))
            else:
                curr_moveset = ()
                prev_moveset = moveset_generator(n//2)
                for move in prev_moveset:
                    curr_moveset += (move*2,)
                    # print(curr_moveset)
                for move in prev_moveset:
                    zero_padding_len = n//2
                    new_move = (move + ((0,) * zero_padding_len),)
                    curr_moveset += new_move
                    # print(curr_moveset)
            return curr_moveset

        # Remove the move that solely consists of 1s in index 0
        moveset_for_n_coins = moveset_generator(n)[1:]
        return moveset_for_n_coins
    
    def generate_move_order(n):
        """ Generates a tuple consisting of the order of moves to be made.
        """
        moveset = generate_moves_for_n_coins(n)
        move_order = ()
        n_minus_1th_move_order = ()
        total_num_of_moves = n-1
        highest_index = total_num_of_moves - 1
        curr_index = 0

        while curr_index <= highest_index:
            indexth_move = moveset[curr_index]
            move_order += (indexth_move,)
            move_order += n_minus_1th_move_order
            n_minus_1th_move_order = move_order
            curr_index += 1
        return move_order

    def main():
        solved = check_solved(table)
        if not solved:
            num_of_coins = get_table_size(table)
            move_order = generate_move_order(num_of_coins)
            # print(f"No. of moves for {num_of_coins} coins: {len(move_order)}")
            for move in move_order:
                flip_coins(table, move)
                solved = check_solved(table)
                if solved:
                    break

    return main()
        

# test:
t4_5 = create_table(4)
solve(t4_5)
print(f"Task 5 test 1: {check_solved(t4_5)}")

t8_5 = create_table(8)
solve(t8_5)
print(f"Task 5 test 2: {check_solved(t8_5)}")

t16_5 = create_table(16)
solve(t16_5)
print(f"Task 5 test 3: {check_solved(t16_5)}")

# Note: It is not advisable to execute run() if the table is large.
