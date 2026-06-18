import random

# --- Board state -----------------------------------------------------------
# A board is just a flat list of 9 cells: indices 0-8, left-to-right, top-to-bottom.
EMPTY = ' '

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def new_board():
    return [EMPTY] * 9


def print_board(board):
    for r in range(0, 9, 3):
        print(f" {board[r]} | {board[r+1]} | {board[r+2]} ")
        if r < 6:
            print("-----------")


def print_index_guide():
    print("Slot numbers:")
    guide = [str(i) for i in range(9)]
    print_board(guide)


# --- Game rules ------------------------------------------------------------
def available_moves(board):
    return [i for i in range(9) if board[i] == EMPTY] # returns a list of non-empty indexes


def winner(board):
    """Return 'O' or 'X' if someone has won, else None."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


# --- Players ---------------------------------------------------------------
def human_move(board, symbol):
    print_index_guide()
    while True:
        raw = input(f"{symbol}'s turn — enter slot (0-8): ")
        if not raw.isdigit():
            print("Please enter a number 0-8.")
            continue
        i = int(raw)
        if 0 <= i <= 8 and board[i] == EMPTY:
            return i
        print("That slot isn't available, try again.")


def minimax(board, current):
    winner = winner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if is_full(board):
        return 0

    nxt = 'X' if current == 'O' else 'O'
    scores = []
    for move in available_moves(board):
        child = board.copy()
        child[move] = current
        scores.append(minimax(child, nxt))   # one number per legal move

    if current == 'O':
        return max(scores)
    else:
        return min(scores)







def bot_move(board, symbol):
    print(minimax(board))


# --- Game loop -------------------------------------------------------------
def play(players):
    """players maps each symbol to a move function: {'O': human_move, 'X': bot_move}"""
    board = new_board()
    current = 'O'  # O always goes first

    while True:
        # Only show the board when a human is about to move. A bot's move is
        # revealed in the next human turn's board (or at game over), so it
        # appears instantly instead of triggering its own redundant print.
        if players[current] is human_move:
            print_board(board)

        move = players[current](board, current)
        board[move] = current

        win = winner(board)
        if win or is_full(board):
            print_board(board)
            print(f"{win} wins!" if win else "Draw!")
            return

        current = 'X' if current == 'O' else 'O'


def main():
    mode = input("1 - Human vs Human\n2 - Human vs Random Bot\nChoose: ")

    if mode == "2":
        human_starts = input("Do you want to start? y/n ").lower() != "n"
        # Human is O (first) if they start, otherwise human is X.
        if human_starts:
            players = {'O': human_move, 'X': bot_move}
        else:
            players = {'O': bot_move, 'X': human_move}
    else:
        players = {'O': human_move, 'X': human_move}

    play(players)


if __name__ == "__main__":
    main()