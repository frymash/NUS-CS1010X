#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    return [[0 for i in range(n)] for i in range(n)]

def has_zero(mat):
    return 0 in flatten(mat)

def add_two(mat):
    def find_zero_pos(lst):
        result = []
        for i in range(len(lst)):
            if lst[i] == 0:
                result.append(i)
        return result

    # Find all zero locations and randomly pick one zero to be
    # replaced by a 2.
    zero_locs = list(map(lambda row: find_zero_pos(row), mat))
    zero_locs = list(map(lambda row: (zero_locs.index(row), row), zero_locs))
    zero_locs = list(filter(lambda row: len(row[1]) != 0, zero_locs))
    # print(f"zero_locs: {zero_locs}")

    if zero_locs == []:
        return mat
    else:
        random_row = choice(list(map(lambda loc: loc[0], zero_locs)))
        # print(f"random_row: {random_row}")
        random_elt = choice(list(filter(lambda loc: loc[0] == random_row, zero_locs))[0][1])
        # print(f"random_elt: {random_elt}")
        mat[random_row][random_elt] = 2
        return mat
    



###########
# Task 2  #
###########

def game_status(mat):
    def are_adj_tiles_present():
        for row in mat:
            for i in range(len(row)-1):
                if row[i] == row[i+1]:
                    return True
        return False
    
    elts = flatten(mat)
    if 2048 in elts:
        return "win"
    elif (0 in elts) or are_adj_tiles_present():
        return "not over"
    else:
        return "lose"
    

###########
# Task 3a #
###########

def transpose(mat):
    result = []
    for i in range(len(mat[0])):
        new_row = list(map(lambda row: row[i], mat))
        result.append(new_row)
    return result



###########
# Task 3b #
###########

def reverse(mat):
    result = []
    for row in mat:
        new_row = row.copy()
        new_row.reverse()
        result.append(new_row)
    return result



############
# Task 3ci #
############

def merge_left(mat):
    new_mat = new_game_matrix(len(mat[0]))
    filtered_mat = [list(filter(lambda x: x != 0, row)) for row in mat]
    score = 0
    skip_next_iteration = False
    for i in range(len(filtered_mat)):
        for j in range(len(filtered_mat[i])):
            if not skip_next_iteration:
                current_tile = filtered_mat[i][j]
                next_tile = False if j+1 > len(filtered_mat[i])-1 else filtered_mat[i][j+1]
                if not next_tile or next_tile != current_tile:
                    new_mat[i][new_mat[i].index(0)] = current_tile
                else:
                    
                    new_mat[i][new_mat[i].index(0)] = next_tile + current_tile
                    score += (next_tile + current_tile)
                    skip_next_iteration = True
            else:
                skip_next_iteration = False
    return (new_mat, new_mat != mat, score)



#############
# Task 3cii #
#############

def merge_right(mat):
    reversed_mat = reverse(mat)
    new_mat, is_valid, score_increment = merge_left(reversed_mat)
    result = (reverse(new_mat), is_valid, score_increment)
    return result

"""
merge_right([[2, 2, 0, 2],
             [4, 0, 0, 0],
             [4, 8, 0, 4],
             [0, 0, 0, 2]])

Result matrix:  [[0, 0, 2, 4],
                 [0, 0, 0, 4],
                 [0, 4, 8, 4],  
                 [0, 0, 0, 2]]
"""

def merge_up(mat):
    transposed = transpose(mat)
    new_mat, is_valid, score_increment = merge_left(transposed)
    result = (transpose(new_mat), is_valid, score_increment)
    return result

"""
merge_up([[2, 2, 0, 2],
          [4, 0, 0, 0],
          [4, 8, 0, 4],
          [0, 0, 0, 2]])

Result matrix:  [[2, 2, 0, 2],
                 [8, 8, 0, 4],
                 [0, 0, 0, 2],  
                 [0, 0, 0, 0]]
"""

def merge_down(mat):
    transposed = transpose(mat)
    new_mat, is_valid, score_increment = merge_right(transposed)
    result = (transpose(new_mat), is_valid, score_increment)
    return result

"""
merge_down([[2, 2, 0, 2],
            [4, 0, 0, 0],
            [4, 8, 0, 4],
            [0, 0, 0, 2]])

Result matrix:    [[0, 0, 0, 0],
                   [0, 0, 0, 2],
                   [2, 2, 0, 4],  
                   [8, 8, 0, 2]]
"""


###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
# text_play()


# How would you test that the winning condition works?
# Your answer:
#
# The game would register a win if game_status(mat)
# (where mat is the game matrix) returns "win".
# Hence, to verify if the winning condition works,
# we must pass a matrix that contains the value 2048
# in any of its rows/columns to game_status and ensure
# it returns "win".
#
# Alternatively, we could try playing the 2048 game
# and check if the game registers a win when the 2048 tile appears.


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return (matrix, total_score)

def get_matrix(state):
    """ Returns the current game matrix. It should be a list of lists as
    per the first part of the mission.
    """
    return state[0]

def get_score(state):
    """ Return the score of the current game as an integer.
    """
    return state[1]
    

def make_new_game(n):
    """ Creates a representation of the game state for a new game. n is the
    size of the game matrix and make_new_game should add the two starting tiles to the
    game.
    """
    new_mat = new_game_matrix(n)
    for i in range(2):
       add_two(new_mat)
    game_state = make_state(new_mat, 0)
    # print(f"game_state: {game_state}")
    return game_state

def slide(merging_fn, state):
    """ Slides the tiles within the game state's matrix in the direction
    stipulated by merging_fn.
    """
    mat = get_matrix(state)
    score = get_score(state)
    new_mat, is_valid, score_increment = merging_fn(mat)
    if is_valid:
        add_two(new_mat)
    new_score = score + score_increment
    game_state = make_state(new_mat, new_score)
    return (game_state, is_valid)

def left(state):
    return slide(merge_left, state)
    
def right(state):
    return slide(merge_right, state)

def up(state):
    return slide(merge_up, state)

def down(state):
    return slide(merge_down, state)


# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    "Your answer here"

def get_record_matrix(record):
    "Your answer here"

def get_record_increment(record):
    "Your answer here"

############
# Task 5ii #
############

def make_new_records():
    "Your answer here"

def push_record(new_record, stack_of_records):
    "Your answer here"

def is_empty(stack_of_records):
    "Your answer here"

def pop_record(stack_of_records):
    "Your answer here"

#############
# Task 5iii #
#############

"""
# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    "Your answer here"

def get_matrix(state):
    "Your answer here"

def get_score(state):
    "Your answer here"

def make_new_game(n):
    "Your answer here"

def left(state):
    "Your answer here"

def right(state):
    "Your answer here"

def up(state):
    "Your answer here"

def down(state):
    "Your answer here"

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    "Your answer here"

def undo(state):
    "Your answer here"
"""


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
##game_logic = {
##    'make_new_game': make_new_game,
##    'game_status': game_status,
##    'get_score': get_score,
##    'get_matrix': get_matrix,
##    'up': up,
##    'down': down,
##    'left': left,
##    'right': right,
##    'undo': undo
##}
#gamegrid = GameGrid(game_logic)
