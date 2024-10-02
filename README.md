# Tic-Tac-Toe Game

This project is a simple console-based implementation of the classic **Tic-Tac-Toe** game. It allows two players to play against each other on a 3x3 grid, where players take turns to place their marks (X or O) until one of them wins or the game ends in a draw.

## How to Play

1. The game starts with an empty 3x3 board.
2. Player 1 is assigned the mark **X** and Player 2 is assigned **O**.
3. Players take turns to input the row and column number to place their marks.
4. The game checks for a winner or a draw after each turn.

### Game Rules

- A player wins by placing three of their marks in a horizontal, vertical, or diagonal row.
- If all the spots are filled and no player has won, the game ends in a draw.

## Project Structure

- **print_board**: Displays the current state of the game board.
- **make_move**: Updates the board with the player's move.
- **get_cells**: Retrieves specific cells from the board to check for a winning combination.
- **is_group_complete**: Checks if a group of cells (row, column, or diagonal) is completely filled.
- **are_all_cells_the_same**: Determines if all the cells in a group are the same (i.e., player has won).
- **is_game_over**: Checks if the game has ended with a win or draw.
- **play_game**: The main function that runs the game loop, allowing players to make moves until the game is over.

## Running the Game

To play the game, simply run the Python script:

## License

This project is licensed under the MIT License. 

```bash
python tic_tac_toe.py
