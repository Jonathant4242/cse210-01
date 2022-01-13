# #Your program must also meet the following requirements.


# The program must have at least one if/then block.
# The program must have at least one while loop.
# The program must have more than one function.
# The program must have a function called main.

# The program must have a comment with assignment and author names.
# Author: Jonathan Trok

ROW_INDEX = 0
COLUMN_INDEX = 1

def main():
    print('Shall we play a game?')
    grid_size = input('What size grid would you like play?')
    grid_size = int(grid_size)
    grid = initialize_grid(grid_size)
    # for i in range(grid_size): - test initialize_grid
    #     print(grid[i])
    play_game(grid, grid_size)
    


def display_game_grid(grid, grid_size):
    cell_width = 5

    row_delimiter = ""
    for column in range(grid_size):
        if column > 0:
            row_delimiter += "+"
        for i in range(cell_width):
            row_delimiter += "-"

    for row in range(grid_size):
        if row > 0:
            print(row_delimiter)
        grid_row = grid[row]
        row_str = ""
        for column in range(grid_size):
            if column > 0:
                row_str += "|"
            cell_value = grid_row[column]
            cell_value = str(cell_value)
            row_str += cell_value.center(cell_width, " ")
        print(row_str)

def get_move_input(grid, grid_size):
    row = 0
    column = 0
    input_valid = False
    max_value = grid_size ** 2
    while not input_valid:
        try:
            cell_num = int(input("Where do you want to move? "))
            cell_num -= 1
        except ValueError:
            cell_num = -1
        if cell_num >= 0 and cell_num < max_value:
            row = int(cell_num / grid_size)
            column = cell_num % grid_size
            grid_row = grid[row]
            if grid_row[column] == "X" or grid_row[column] == "O":
                print("Square already taken. Try again.")
            else:
                input_valid = True
        else:
            print("Invalid choice. Try again.")



    return (row, column)

def initialize_grid(grid_size):
    value = 1
    grid = {}
    for row in range(grid_size):
        row_dic = {}
        for column in range(grid_size):
            row_dic[column] = value
            value += 1
        grid[row] = row_dic
    return grid

def check_for_winner(grid, grid_size, move):
    game_over = False
    # Check row
    grid_row = grid[move[ROW_INDEX]]
    value = grid_row[move[COLUMN_INDEX]]
    winner = True
    for column in range(grid_size):
        if grid_row[column] != value:
            winner = False
            break
    if winner:
        game_over = True
        print(f"winner row {move[ROW_INDEX]}")

    # Check column
    column = move[COLUMN_INDEX]
    winner = True
    for row in range(grid_size):
        grid_row = grid[row]
        if value != grid_row[column]:
            winner = False
            break
    if winner:
        game_over = True
        print(f"winner column {column}")

    # Check diagnol 1
    winner = True
    if move[ROW_INDEX] == move[COLUMN_INDEX]:
        for index in range(grid_size):
            grid_row = grid[index]
            if value != grid_row[index]:
                winner = False
                break
        if winner:
            game_over = True
            print("winner diag 1")

    # Check diagnol 2
    winner = True
    if (move[ROW_INDEX] + move[COLUMN_INDEX]) == (grid_size - 1):
        for index in range(grid_size):
            grid_row = grid[(grid_size-1) - index]
            if value != grid_row[index]:
                winner = False
                break
        if winner:
            game_over = True
            print("winner diag 2")

    return game_over

def play_game(grid, grid_size):
    num_moves = 0
    max_moves = grid_size ** 2
    player = "O"
    game_over = False
    while not game_over:
        if player == "X":
            player = "O"
        else:
            player = "X"
        display_game_grid(grid, grid_size)
        print()
        print()
        print(f"Player {player}'s turn")
        move = get_move_input(grid, grid_size)
        row = grid[move[ROW_INDEX]]
        row[move[COLUMN_INDEX]] = player
        game_over = check_for_winner(grid, grid_size, move)
        num_moves += 1
        if num_moves == max_moves:
            game_over = True
    
    display_game_grid(grid, grid_size)
    if num_moves == max_moves:
        print("Cat's game. Meow - no one won")
    else:
        print(f"Player {player} wins! Congratulations.")

main()