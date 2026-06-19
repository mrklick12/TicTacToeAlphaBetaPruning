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
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
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
        else:
            if board[slot] != EMPTY:
                print("That slot isn't free, try again.")
            else:
                return slot
        
def bot_move(board):
    return random.choice(available_moves(board))

def game_ended(board, current):
    if winner(board):
        print_board(board)
        print(f"{current} wins!")
        return True
    elif is_full(board):
        print_board(board)
        print("Draw!")
        return True


def play(options):
    board = new_board()
    current = 'O' # O always starts.
    gameContinue = True

    while gameContinue:
        if options[0]: # Human Vs Human
            print_board(board)
            board[player_move(board, current)] = current

            hasGameEnded = game_ended(board, current)
            if hasGameEnded:
                gameContinue = not hasGameEnded

        elif options[1]: # Human Starting Against A Bot
            print_board(board)
            board[player_move(board, current)] = current
            hasGameEnded = game_ended(board, current)
            if hasGameEnded:
                gameContinue = not hasGameEnded
            current = 'X' if current == 'O' else 'O'
            board[bot_move(board)] = current
            hasGameEnded = game_ended(board, current)
            if hasGameEnded:
                gameContinue = not hasGameEnded
        elif options[2]:
            board[bot_move(board)] = current
            hasGameEnded = game_ended(board, current)
            if hasGameEnded:
                return
            current = 'X' if current == 'O' else 'O'
            print_board(board)
            board[player_move(board, current)] = current
            hasGameEnded = game_ended(board, current)
            if hasGameEnded:
                gameContinue = not hasGameEnded

            
        current = 'X' if current == 'O' else 'O'
        
            

        
            


    


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

main()