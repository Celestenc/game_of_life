import random
from time import sleep


# Storing the board state
    
# Creating matrix with all 0s, ie all cells are dead
def dead_state(width, height):
    board_matrix = [[0 for i in range(width)] for j in range(height)]
    return board_matrix

# Create a random initial board state
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


# Rendering any board state ie pretty-printing board to terminal
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


# Calculating next board state
def next_board_state(init_state):
    width = len(init_state[0])
    height = len(init_state)
    next_state = dead_state(width, height)

    for x in range(height):
        for y in range(width):
            current_cell_value = init_state[x][y]
            counter = 0

            # Iterating around every cell and taking into account edges
            for k in range(max(x - 1, 0), min(x + 2, height)):
                for l in range(max(y - 1,0), min(y + 2, width)):
                    if k == x and l == y:
                        continue
                    if init_state[k][l] == 1:
                        counter += 1
            
            # Updating dead_state board
            if current_cell_value == 1:
                if counter <= 1 or counter > 3:
                    next_state[x][y] = 0
                else:
                    next_state[x][y] = 1
            else: # Checking for last condition
                if counter == 3:
                    next_state[x][y] = 1
    
    return next_state

# Handling designs from txt files
def load_board_state(txt_file):
    life_board = []
    with open(txt_file) as life:
        for x in life:
            life_row = []
            for y in x:
                if y != '\n':
                    life_row.append(int(y))
            life_board.append(life_row)

    return life_board

# Printing Cellular Automata designs from txt.file
start_state = load_board_state("./gosper_glider_gun.txt")
render(start_state)
next_drawing = next_board_state(start_state)
render(next_drawing)

# Forever printing the next board
while True:
    next_drawing = next_board_state(next_drawing)
    render(next_drawing)
    sleep(0.2)
