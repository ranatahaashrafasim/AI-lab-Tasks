board = [" "] * 9

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def win(player):
    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player or
        board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player or
        board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True
    return False

player = "X"
moves = 0

while True:
    display()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos >= 0 and pos <= 8 and board[pos] == " ":
        board[pos] = player
        moves += 1

        if win(player):
            display()
            print("Player", player, "wins")
            break

        if moves == 9:
            display()
            print("Match Draw")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("Invalid move, try again")