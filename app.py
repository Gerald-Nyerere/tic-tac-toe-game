import random
 
board = ["-" for _ in range(9)]
current_player = "X"
winner = None
game_running = True
 
# printing game boARD
def print_board(board):
    print( board[0] +  "|" +  board[1]  +  "|"  +  board[2])
    print("------")
    print( board[3] +  "|"  + board[4]  +  "|"  +  board[5])
    print("------")
    print( board[6] +  "|"  + board[7]  +  "|"  +  board[8])
    
print_board(board)
 
# TAKE PLAYER INPUT
def player_input(board):
    players_input = int(input("Enter a number 1-9: " ))
    if players_input >= 1 and players_input <= 9 and board[players_input-1] == "-":
        board[players_input] = current_player
    else:
        print("spot already taken!")
# check for win or tie
def check_horzontal(board):
    global winner
    if board[0] == board[1] == board[2] and  board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and  board[6] != "-":
        winner =  board[6]
        return True
    
def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and  board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and  board[2] != "-":
        winner =  board[2]
        return True
    
def check_diagnol(board):
    global winner
    if board[0] == board[4] == board[8] and  board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
def draw(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("it is a draw")
        game_running = False
 
def check_win(board):
    if check_diagnol(board) or check_horzontal(board) or check_row(board):
        print(f"The winner is {winner} ")
#switch the player
def switch_player():
    global current_player 
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
# function for computer to play
def computer(board):
    while current_player == "O":
        choice = random.randint(0, 8)
        if board[choice] == "-":
            board[choice] = "O"
            switch_player()
#check for win or tie again
while game_running:
    print_board(board)
    player_input(board)
    check_win(board)
    draw(board)
    switch_player()
    computer(board)
    check_win(board)
    draw(board)