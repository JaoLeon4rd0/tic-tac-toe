from random import randrange

def init_board(board): 
    num = 0
    for line in range(3): 
        board.append([])
        for column in range(3): 
            num+=1
            if num != 5: 
                board[line].append(num)
            else: 
                board[line].append('X')
                
    return board 

def display_board(board):
   
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    for line in board:
        print("+------+-------+-------+") 
        print("|      |       |       |")
        print("|  ", line[0], " |  ", line[1], "  |  ", line[2], "  |")
        print("|      |       |       |")
    print("+------+-------+-------+")

def enter_move(board):
    
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    
    found = False 
    
    while not found:
        
        move = int(input("Enter your move: "))
        
        if move < 0 and > 9:
            return print("Invalid Number!")
        
        free_fields = make_list_of_free_fields(board)
        
        
        
        for row, column in free_fields: 
            if board[row][column] == move: 
                board[row][column] = 'O'
                found = True
            
        if not found: 
            print("Squares already filled!")

def make_list_of_free_fields(board):
    
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    free_fields = []
    
    for line in range(len(board)):
        for column in range(len(board[line])): 
            if board[line][column] != 'X' and board[line][column] != 'O':
                field = line, column,
                free_fields.append(field)
                
    return free_fields            

def victory_for(board, sign):
    
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    pass

def draw_move(board):
    
    # The function draws the computer's move and updates the board.
    print("Funciona")


sign = True
board = []
board = init_board(board)

display_board(board)

while sign: 
    
    enter_move(board)
    
        

