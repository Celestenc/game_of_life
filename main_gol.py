import random

# Milestone 1: Storing the board state
    
# Creating matrix with all 0s, ie all cells are dead
def dead_state(width, height):
    board_matrix = [[0 for i in range(width)] for j in range(height)]
    return board_matrix

def random_state(width, height):
    # Build board using previous work
    state = dead_state(width, height)

    # Randomize each element of "state"
    for x in range(len(state)):
        for y in range(len(state[x])):
            random_number = random.random()

            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            
            state[x][y] = cell_state
    
    return state

# Mileston 2: Pretty-printing board to terminal

# Rendering any board state
def render(board_state):
    top_bottom_edge = "-" * (len(board_state[0]) + 2)
    print(top_bottom_edge) 
    for x in board_state:
        print("|", end = "")
        for y in x:
            if y == 1:
                print("#", end = "")
            else:
                print(" ", end = "")
        print("|")
    print(top_bottom_edge) 

a_dead_state = dead_state(5,5)
render(a_dead_state)

a_random_state = random_state(10, 5)
render(a_random_state)
