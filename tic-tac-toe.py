# Function to print the board
def print_board(board):
    formatted_rows = []
    for row in board:
        formatted_rows.append(" ".join(row))
    grid = "\n".join(formatted_rows)
    return grid

# Function to make a move
def make_move(board, row, column, player):
    if board[row][column] == ".":
        board[row][column] = player
    else:
        print("That spot is already taken. Try again.")
    return board

# Function to get specific cells from the board
def get_cells(board, coord_1, coord_2, coord_3):
    return [
        board[coord_1[0]][coord_1[1]],
        board[coord_2[0]][coord_2[1]],
        board[coord_3[0]][coord_3[1]]
    ]

# Function to check if a group of cells is complete
def is_group_complete(board, coord_1, coord_2, coord_3):
    cells = get_cells(board, coord_1, coord_2, coord_3)
    return "." not in cells

# Function to check if all cells in a group are the same
def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
    cells = get_cells(board, coord_1, coord_2, coord_3)
    return cells[0] == cells[1] and cells[1] == cells[2]

# List of groups to check (rows, columns, diagonals)
groups_to_check = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

# Function to check if the game is over
def is_game_over(board):
    for group in groups_to_check:
        if is_group_complete(board, group[0], group[1], group[2]):
            if are_all_cells_the_same(board, group[0], group[1], group[2]):
                return True
    return False

# Main function to play the game
def play_game():
    board = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]
    player = "X"
    while not is_game_over(board):
        print(print_board(board))
        print(f"It's {player}'s turn.")
        try:
            row = int(input("Enter a row (0, 1, or 2): "))
            column = int(input("Enter a column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if 0 <= row <= 2 and 0 <= column <= 2:
            board = make_move(board, row, column, player)
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("Invalid input. Please enter numbers between 0 and 2.")

    print(print_board(board))
    print("Game over!")

# Start the game
print("Game time!")
play_game()
