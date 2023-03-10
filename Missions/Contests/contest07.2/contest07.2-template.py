#
# CS1010X --- Programming Methodology
#
# Contest 7.2 Template

from more_lazy_susan import *

def create_solver(coins):
    # insert your code here
    move = [True] + [False] * (coins - 1)
    
    def solver(move_id):
        # insert your code here
        return move

    return solver


# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
#get_contest_score(create_solver, True)
