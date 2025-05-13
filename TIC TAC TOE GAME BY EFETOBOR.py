# JESUS IS LORD!
# TIC TAC TOE GAME BY ME!!
# PLEASE FOLLOW ON INSTAGRAM @tobor._

def display_sample_board():
    """Prints a sample board with positions."""
    sample_board = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print_board(sample_board)

def print_board(board):
    """Prints the current game board."""
    print('\n' * 3)
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("---------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("---------")
    print(f"{board[7]} | {board[8]} | {board[9]}")

def player_input():
    """Gets a valid position input from the player."""
    while True:
        try:
            position = int(input("Please input a position (1-9): "))
            if position in range(1, 10):
                return position
            else:
                print("Invalid input. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play(position, board, marker):
    """Places the player's marker on the board."""
    while board[position] != ' ':
        print("This position is already taken. Try another space!")
        position = player_input()
    board[position] = marker

def check_winner(board, marker):
    """Checks if the given marker has won."""
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    return any(all(board[pos] == marker for pos in combo) for combo in win_combinations)

def is_draw(board):
    """Checks if the game is a draw."""
    return ' ' not in board[1:]

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    print("Welcome to Tic Tac Toe!")
    display_sample_board()

    board = [' '] * 10
    print_board(board)

    tries = 0
    while True:
        # Player X's turn
        print("Player X's turn:")
        position = player_input()
        play(position, board, 'X')
        tries += 1
        print_board(board)

        if check_winner(board, 'X'):
            print("X wins!!!!!!!!!")
            break
        if tries == 9:
            print("It's a draw!")
            break

        # Player O's turn
        print("Player O's turn:")
        position = player_input()
        play(position, board, 'O')
        tries += 1
        print_board(board)

        if check_winner(board, 'O'):
            print("O wins!!!!!!!!!")
            break
        if tries == 9:
            print("It's a draw!")
            break

# Run the game
tic_tac_toe()
