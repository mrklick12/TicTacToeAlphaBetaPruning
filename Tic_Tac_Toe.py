import random

EMPTY = ' '

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]

def new_board():
    return [EMPTY] * 9


def print_board(board):
    for i in range(0,9,3):
        print(str(board[i]) + " | " + str(board[i+1]) + " | " + str(board[i+2]))
        if i < 6:
            print("---------")

def print_template_board():
    print("Slot Numbers: ")
    template = [0,1,2,3,4,5,6,7,8,9]
    print_board(template)

def available_moves(board):
    moves = []
    for i, move in enumerate(board):
        if move == EMPTY:
            moves.append(i)
    return moves


def winner(board): # returns the symbol of the winner
    for a,b,c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a]
        return None

def is_full(board):
    if EMPTY not in board:
        return True
    return False

def player_move(board, symbol):
    print_template_board()
    while True:
        slot = int(input(f"{symbol}'s turn - Enter slot:"))
        if slot < 0 or slot > 8:
            print("Please enter a number between 0-8.")
            continue
        else:
            if board[slot] == EMPTY:
                print("That slot isn't free, try again.")
            else:
                return slot
        

def play(options):
    board = new_board()
    current = 'O' # O always starts.

    if options[0]:
        

    


def main():
    mode = input("1 - Human vs Human\n2 - Human vs Random Bot\nChoose: ")
    options = (1, 0, 0) 
    # (HumanVsHuman, HumanVsComputer - human starts, ComputerVsHuman - computer starts)
    if mode == "2":
        human_starts = input("Do you want to start? y/n ").lower() != "n"
        # Human is O (first) if they start, otherwise human is X.
        if human_starts:
            options = (0, 1, 0)
        else:
            options = (0, 0, 1)

    play(options)