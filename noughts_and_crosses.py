board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
turn = "X"

def get_coords():
    try:
        coords = [int(coord) for coord in input("Enter the X and Y co-ordinates (x,y): ").strip().split(",")]
        assert len(coords) == 2
        return coords
    except (ValueError, AssertionError):
        print("Invalid answer, please enter it correctly.")
        return get_coords()
    except KeyboardInterrupt:
        print()
        exit()

def print_board():
    print(f"[{board[0][0]} {board[0][1]} {board[0][2]}]")
    print(f"[{board[1][0]} {board[1][1]} {board[1][2]}]")
    print(f"[{board[2][0]} {board[2][1]} {board[2][2]}]")
    print()

x_win_row = ["X", "X", "X"]
y_win_row = ["Y", "Y", "Y"]
def check_win():
    # Rows
    for row in board:
        if row == x_win_row:
            return "X"
        if row == y_win_row:
            return "Y"

    # Columns
    for col_num in range(3):
        if board[0][col_num] == board[1][col_num] and board[1][col_num] == board[2][col_num] and board[0][col_num] != " ":
            return board[0][col_num]

    # Diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        return board[col_num][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return " "


while True:
    print("Current board:")
    print_board()
    [x, y] = get_coords()
    board[x][y] = turn
    if turn == "X":
        turn = "Y"
    else:
        turn = "X"
    
    winner = check_win()
    if winner == "X" or winner == "Y":
        print(f"The winner is {winner}!")
        print_board()
        exit()