board = [" " for _ in range(9)]
print(board)

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def player_input(player):
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= position <= 8 and board[position] == " ":
                return position
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def check_win():
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

def play():
    player = "X"
    turn = 0

    while True:
        display_board()
        position = player_input(player)
        board[position] = player
        turn += 1

        if check_win():
            display_board()
            print(f"Player {player} wins!")
            break

        if turn == 9:
            display_board()
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"


play()