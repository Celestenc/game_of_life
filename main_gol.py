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


print(random_state(5,5))
