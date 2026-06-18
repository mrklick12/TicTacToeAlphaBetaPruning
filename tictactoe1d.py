board = []
for i in range(9):
    board.append(' ')

def print_board():
    line = "---------"
    row = ""
    j = 0
    for i in range(9):
        if j < 2:
            row += board[i] + ' | '
            j += 1
        else:
            row += board[i]
            j = 0
            row = ""
        print(row)
        print(line)

def template_board():
    print("Please Select Number (0-8): ")
    row = ""
    num = 0
    j = 0
    line = "---------"
    for i in range(9):
        if j < 2:
            row += str(num) + ' | '
            j += 1
        else:
            row += str(num)
            j = 0
            row = ""
            print(row)
            print(line)
        num += 1
        
        

def validate_input(index):


    if index > 8 or index < 0 or board[index] != ' ':
        print("Invalid Input.")
        template_board()
        choice = input("Enter Slot: ")
        validate_input(choice)
    

def update_board(user1Turn, index):

    if user1Turn:
        board[index] = 'O'
    else:
        board[index] = 'X'
    print_board()


def check_win():
    print("")
    

user1turn = True # User 1 is always O, User 2 is alwasy X
gameContinue = True

template_board()

while gameContinue:
    if user1turn:
        print("O's Turn")
    else:
        print("X's Turn")
    
    choice = int(input("Enter Slot: "))
    validate_input(choice)

    update_board(user1turn, choice)
    user1turn = not user1turn
    template_board()

