from main_gol import next_board_state

def message(init_state, expected_next_state, test_num):

    actual_next_state = next_board_state(init_state)

    if expected_next_state == actual_next_state:
        print("PASSED " + str(test_num))
    else:
        print("FAILED " + str(test_num) + "!")
        print("Expected:")
        print(expected_next_state)
        print("Actual:")
        print(actual_next_state)
    

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    message(init_state1, expected_next_state1, 1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    message(init_state2, expected_next_state2, 2)
