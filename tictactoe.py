import random

board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(' ')
    board.append(row)

def print_board():
    line = "---------"
    for i in range(3):
        row = ""
        for j in range(3):
            if j < 2:
                row += board[i][j] + ' | '
            else:
                row += board[i][j]
        print(row)
        print(line)

def template_board():
    print("Please Select Number (0-8): ")
    num = 0
    line = "---------"
    for i in range(3):
        row = ""
        for j in range(3):
            if j < 2:
                row += str(num) + ' | '
            else:
                row += str(num)
            num += 1
        print(row)
        print(line)

def validate_input(index):
    row = index // 3
    column = index % 3
    
    if index > 8 or index < 0 or board[row][column] != ' ':
        print("Invalid Input.")
        template_board()
        choice = int(input("Enter Slot: "))
        validate_input(choice)
    

def update_board(user1Turn, index):
    row = index // 3
    column = index % 3

    if user1Turn:
        board[row][column] = 'O'
    else:
        board[row][column] = 'X'
    
    

def random_computer_move(isComputerStarting):
    rindex = random.randint(0,8)
    row = rindex // 3
    column = rindex % 3

    if board[row][column] != ' ':
        random_computer_move(isComputerStarting)
    else:
        if isComputerStarting:
            board[row][column] = 'O'
        else:
            board[row][column] = 'X'

def check_win():
    listBoard = []
    for row in board:
        for item in row:
            listBoard.append(item)

    def horizontal_win():
        for i in range(0,8,3):
            if listBoard[i] == listBoard[i+1] == listBoard[i+2]:
                if listBoard[i] != ' ':
                    return True
        return False
    def vertical_win():
        for i in range(3):
            if listBoard[i] == listBoard[i+3] == listBoard[i+6]:
                if listBoard[i] != ' ':
                    return True
        return False
    def diagonal_win():
        # hard coding bc i cba
        if listBoard[0] == listBoard[4] == listBoard[8]:
            if listBoard[0] != ' ':
                return True
        elif listBoard[2] == listBoard[4] == listBoard[6]:
            if listBoard[2] != ' ':
                return True
        else:
            return False
        
    if horizontal_win() or diagonal_win() or vertical_win():
        return True
    else:
        return False


def check_draw():
    size = 0
    for row in board:
        for item in row:
            if item != ' ':
                size += 1
    if size == 9:
        return True
        
def check_end_game(user1turn, msg1, msg2):
    if check_win():
        if user1turn:
            print(msg1)
        else:
            print(msg2)
        return True
    elif check_draw():
        print("DRAW!")
        return True
    return False

user1turn = True # User 1 is always O, User 2 is alwasy X
isComputerStarting = False
gameContinue = True

option = input("1 - Human vs Human\n2 - Human vs Random Bot")
if option == "2":
    optionToStart = input("Do you want to start? y/n")
    if optionToStart == "n":
        isComputerStarting = True
        random_computer_move(isComputerStarting)
        print_board()



template_board()

while gameContinue:
    if option == "1":
        if user1turn:
            print("O's Turn")
        else:
            print("X's Turn")
        
        choice = int(input("Enter Slot: "))
        validate_input(choice)

        update_board(user1turn, choice)
        print_board()

        if check_end_game(user1turn, "Player O WIN!", "Player X Win!"):
            gameContinue = False
        else:
            user1turn = not user1turn
            template_board()

    elif option == "2":
        print("Players Turn: ")
        choice = int(input("Enter Slot: "))
        validate_input(choice)
        update_board(not isComputerStarting, choice)
        if check_win():
            print_board()
            print("Player Won!")
            gameContinue = False
        elif check_draw():
            print_board()
            print("Draw")
            gameContinue = False
        else:
            random_computer_move(isComputerStarting)
            print_board()
            if check_win():
                print("Computer Won Won!")
                gameContinue = False
            elif check_draw():
                print("Draw")
                gameContinue = False
        

