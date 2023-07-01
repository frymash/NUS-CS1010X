def play(game_state,player):
    display_game_state(game_state)
    if is_game_over(game_state):
        announce_winner(player)
    elif player == "human":
        play(human_move(game_state),"computer")
    elif player == "computer":
        play(computer_move(game_state),"human")
    else:
        print("player wasn't human or computer:",player)

def computer_move(game_state):
    pile = 1 if size_of_pile(game_state,1) > 0 else 2
    print("Computer removes 1 coin from pile "+str(pile))
    return remove_coins_from_pile(game_state, 1, pile)

def prompt(prompt_string):
    return input(prompt_string)

def human_move(game_state):
    p = prompt("Which pile will you remove from?")
    n = prompt("How many coins do you want to remove?")
    return remove_coins_from_pile(game_state, int(n), int(p))

def is_game_over(game_state):
    return total_size(game_state) == 0

def announce_winner(player):
    if player == "human":
        print("You lose. Better luck next time.")
    else:
        print("You win. Congratulations.")

def make_game_state(n,m):
    return (n,m)

def size_of_pile(game_state,pile_number):
    return game_state[pile_number-1]

def remove_coins_from_pile(game_state, num_coins, pile_number):
    if pile_number == 1:
        return make_game_state(size_of_pile(game_state,1) - num_coins,
                               size_of_pile(game_state,2))
    else:
        return make_game_state(size_of_pile(game_state,1),
                               size_of_pile(game_state,2) - num_coins)
	
def display_game_state(game_state):
    print("")
    print(" Pile 1: " + str(size_of_pile(game_state,1)))
    print(" Pile 2: " + str(size_of_pile(game_state,2)))
    print("")
    
def total_size(game_state):
    return size_of_pile(game_state,1)+ size_of_pile(game_state,2)

def start():
    play(make_game_state(5,5),"human")
        
