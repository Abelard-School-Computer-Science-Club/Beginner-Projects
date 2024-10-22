# LIST AND STRING MANIPULATION
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]}")
        if i < 2:
            print("---------")

# WHILE LOOP
current_player = "X"  # Start with player X
for turn in range(9):
    print_board()
    # INPUT STATEMENT
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    # VALIDATE INPUT
    if board[move] != " ":
        print("Invalid move, try again.")
        continue

    board[move] = current_player

    # CHECK FOR WINNING CONDITION
    if (board[0] == board[1] == board[2] == current_player or
        board[3] == board[4] == board[5] == current_player or
        board[6] == board[7] == board[8] == current_player or
        board[0] == board[3] == board[6] == current_player or
        board[1] == board[4] == board[7] == current_player or
        board[2] == board[5] == board[8] == current_player or
        board[0] == board[4] == board[8] == current_player or
        board[2] == board[4] == board[6] == current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break  # Exit the loop if there's a winner
    # SWITCH PLAYER
    current_player = "O" if current_player == "X" else "X"
else:
    print_board()
    print("It's a draw!")