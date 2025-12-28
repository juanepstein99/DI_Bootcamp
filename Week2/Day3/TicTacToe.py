# Step 1: Representing the Game Board

def create_board():
    # Creates an empty 3x3 board (with spaces)
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

# Step 2: Displaying the Game Board

def display_board(board):
    # Displays the current state of the board
    print("   1   2   3")
    for i, row in enumerate(board):
        print(f"{i+1}  " + " | ".join(row))
        if i < 2:
            print("  ---+---+---")

# Step 3: Getting Player Input

def player_input(player, board):
    # Asks the player for a valid move and returns (row, col)
    while True:
        row = input(f"Player {player}, choose a row (1-3): ")
        col = input(f"Player {player}, choose a column (1-3): ")

        # Check if the input contains only digits
        if not row.isdigit() or not col.isdigit():
            print("Please enter numbers only.")
            continue

        # Convert to integers and change from 1-3 to 0-2
        row = int(row) - 1
        col = int(col) - 1

        # Check if the numbers are within the valid range
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Please choose numbers between 1 and 3.")
            continue

        # Check if the chosen cell is empty
        if board[row][col] != " ":
            print("This cell is already taken.")
            continue
        return row, col

# Step 4: Checking for a Winner

def check_win(board, player):
    # Check rows
    for row in board:
        if row == [player, player, player]:
            return True

    # Check columns
    for c in range(3):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Step 5: Checking for a Tie

def check_tie(board):
    # Check if there are no empty spaces left
    for row in board:
        if " " in row:
            return False
    return True

def switch_player(player):
    # Switch between players X and O
    return "O" if player == "X" else "X"

# Step 6: The Main Game Loop

def play():
    board = create_board()   # Create an empty board
    player = "X"            # Start with player X

    while True:
        display_board(board)                   # Show the board
        row, col = player_input(player, board) # Get a valid move
        board[row][col] = player               # Place the player's symbol

        # Check if the player has won
        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break

        # Check if the game is a tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch to the next player
        player = switch_player(player)

play()
