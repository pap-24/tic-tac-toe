# ===========================================================================
# Getting players' choices
# ===========================================================================
def getPlayerChoice(P1_NAME):
        PLAYER_1 = input(f"{P1_NAME}, give your symbol 'X' or 'O': ").upper()
        
        while not (PLAYER_1 == "X" or PLAYER_1 == "O"):
            print("Please enter 'X' or 'O'")
            PLAYER_1 = input(f"{P1_NAME}, give your symbol 'X' or 'O': ").upper()
            
        if PLAYER_1 == "X":
            PLAYER_2 = "O"
        else:
            PLAYER_2 = "X"
        
        return (PLAYER_1, PLAYER_2)
# ===========================================================================

# ===========================================================================
# Set up who plays first
# ===========================================================================
from random import randint

def getPlayerTurn():
    if randint(1, 2) == 1:
        return 'Player 1'
    else:
        return 'Player 2' 
# ===========================================================================

# ===========================================================================
# Getting players' names
# ===========================================================================
def getPlayerNames():
        PLAYER_1_NAME = input("Player 1, give your name: ")
        PLAYER_2_NAME = input("Player 2, give your name: ")
        
        return (PLAYER_1_NAME, PLAYER_2_NAME)
# ===========================================================================

# ===========================================================================
# Display the board
# ===========================================================================
from IPython.display import clear_output

def displayBoard(lista):
    clear_output() # Remember! This only works in jupyter notebook!!
    LINE = '---|---|---'
    # Print everything from the list along with a space at the start
    # to make it look better.
    print(f' {lista[7]} | {lista[8]} | {lista[9]}')
    print(LINE)
    print(f' {lista[4]} | {lista[5]} | {lista[6]}')
    print(LINE)
    print(f' {lista[1]} | {lista[2]} | {lista[3]}')
# ===========================================================================

# =============================================================================================
# Get the current player's position choice
# =============================================================================================
def getPlayerPosition(lista, currentPlayer):
    POSITION = int(input(f"{currentPlayer}, give your place on the board. Select (1 - 9): "))

    while (1 < POSITION > 9) or (lista[POSITION] != " "): # position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(f"{currentPlayer}, the place you gave is taken or the place you entered is not between 1 and 9.")
        POSITION = int(input(f"{currentPlayer}, give your place on the board. Select (1 - 9): "))
    
    return POSITION
# =============================================================================================

# =================================================================================================
# Check if player 1 or player 2 won
# =================================================================================================
def checkWin(lista, mark):
    return (
        (lista[7] == mark and lista[8] == mark and lista[9] == mark) or # Top Horizontal (---)
        (lista[7] == mark and lista[5] == mark and lista[3] == mark) or # Diagonal (\)
        (lista[4] == mark and lista[5] == mark and lista[6] == mark) or # Middle Horizontal (---)
        (lista[9] == mark and lista[5] == mark and lista[1] == mark) or # Diagonal (/)
        (lista[1] == mark and lista[2] == mark and lista[3] == mark) or # Bottom Horizontal (---)
        (lista[7] == mark and lista[4] == mark and lista[1] == mark) or # Left Vertical (|)
        (lista[9] == mark and lista[6] == mark and lista[3] == mark) or # Right Vertical (|)
        (lista[8] == mark and lista[5] == mark and lista[2] == mark)    # Center Vertical (|)
    )        
# =================================================================================================

# =================================================================================================
# Check if the board is full, if it is, it's a TIE.
# =================================================================================================
def checkFullBoard(lista):
    for item in lista:
        if item == " ":
            return False
    return True
# =================================================================================================

# =================================================================================================
# Question to play again or no
# =================================================================================================
def playAgain():
    play = input("Do you want to play again? (Y/N): ")
    ch = "yYnN"
    
    while play not in ch:
        play = input("Wrong choice. Do you want to play again? (Y/N): ")
        
    return play.lower() == 'y'
# =================================================================================================

# ===========================================================================================
# MAIN PROGRAM
# ===========================================================================================
print("Welcome to Tic-Tac-Toe!")

# ÎŸÏÎ¯Î¶Ï‰ Ï„Î·Î½ gameOn True ÎºÎ±Î¹ Ï„Î¿ Ï€Î±Î¹Ï‡Î½Î¯Î´Î¹ Î¾ÎµÎºÎ¹Î½Î¬ÎµÎ¹.
gameOn = True

while gameOn:
    # Î Î¬ÏÎµ Ï„Î± Î¿Î½ÏŒÎ¼Î±Ï„Î± Ï„Ï‰Î½ Ï€Î±Î¹Ï‡Ï„Î„Î„Ï‰Î½
    PLAYER_NAME_1, PLAYER_NAME_2 = getPlayerNames()

    # Î‘ÏÏ‡Î¹ÎºÎ¿Ï€Î¿Î¯Î·ÏƒÎ· Ï„Î¿Ï… board.
    board = ["#"] + [' '] * 9 # board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    # ÎŸÏÎ¯Î¶Ï‰ Ï„Î± ÏƒÏÎ¼Î²Î¿Î»Î± Ï„Ï‰Î½ Î´ÏÎ¿ Ï€Î±Î¹Ï‡Ï„ÏŽÎ½.
    PLAYER_1_MARK, PLAYER_2_MARK = getPlayerChoice(PLAYER_NAME_1)
    
    # ÎšÎ±Î¸Î¿ÏÎ¯Î¶Ï‰ Ï„Î¿Î½ Ï€Î±Î¯Ï‡Ï„Î· Ï€Î¿Ï… Ï€Î±Î„Î¯Î¶ÎµÎ¹ Ï€ÏÏŽÏ„Î¿Ï‚.
    PLAYER_TURN = getPlayerTurn()
    
    Win = False
    Tie = False
    
    # Î¤Î¿ Ï€Î±Î¹Ï‡Î½Î¯Î´Î¹ ÏƒÏ…Î½ÎµÏ‡Î¯Î¶ÎµÏ„Î±Î¹ Î¼Î­Ï‡ÏÎ¹ ÎºÎ¬Ï€Î¿Î¹Î¿Ï‚ Î½Î± ÎºÎµÏÎ´Î¯ÏƒÎµÎ¹ Î® Î½Î± Î­ÏÎ¸ÎµÎ¹ Î¹ÏƒÎ¿Ï€Î±Î»Î¯Î±
    while not (Win or Tie):
        
        # Î•Î¼Ï†Î±Î½Î¯Î¶Ï‰ Ï„Î¿ board.
        displayBoard(board)
        
        if PLAYER_TURN == "Player 1": # Î•Î»Î­Î³Ï‡Ï‰ Ï€Î¿Î¹Î¿Ï‚ Ï€Î±Î¯Ï‡Ï„Î·Ï‚ Ï€Î±Î¯Î¶ÎµÎ¹ (Player 1)
            print(f"\n{PLAYER_NAME_1} PLAYS!")
            
            # ÎŸ Player 1 ÎµÏ€Î¹Î»Î­Î³ÎµÎ¹ Ï„Î· Î¸Î­ÏƒÎ· ÎºÎ±Î¹ Î³ÎµÎ¼Î¯Î¶ÎµÎ¹ Ï„Î¿ board Î¼Îµ Ï„Î¿ ÏƒÏÎ¼Î²Î¿Î»Î¿ Ï€Î¿Ï… Î­Ï‡ÎµÎ¹ Î´Î¹Î±Î»Î­Î¾ÎµÎ¹.
            board[getPlayerPosition(board, PLAYER_NAME_1)] = PLAYER_1_MARK
            
            # Win Check
            if checkWin(board, PLAYER_1_MARK):
                displayBoard(board)
                print(f"Congratulations! {PLAYER_NAME_1}, you won the game!")
                Win = True
                
            # Tie Check
            elif checkFullBoard(board):
                displayBoard(board)
                print('Congratulations to both players! It\'s a TIE!')
                Tie = True
            PLAYER_TURN = 'Player 2'
        
        else: # Î•Î»Î­Î³Ï‡Ï‰ Ï€Î¿Î¹Î¿Ï‚ Ï€Î±Î¯Ï‡Ï„Î·Ï‚ Ï€Î±Î¯Î¶ÎµÎ¹ (Player 2)
            print(f"\n{PLAYER_NAME_2} PLAYS!")
            
            # ÎŸ Player 2 ÎµÏ€Î¹Î»Î­Î³ÎµÎ¹ Ï„Î· Î¸Î­ÏƒÎ· ÎºÎ±Î¹ Î³ÎµÎ¼Î¯Î¶ÎµÎ¹ Ï„Î¿ board Î¼Îµ Ï„Î¿ ÏƒÏÎ¼Î²Î¿Î»Î¿ Ï€Î¿Ï… Î­Ï‡ÎµÎ¹ Î´Î¹Î±Î»Î­Î¾ÎµÎ¹.
            board[getPlayerPosition(board, PLAYER_NAME_2)] = PLAYER_2_MARK
            
            # Win Check
            if checkWin(board, PLAYER_2_MARK):
                displayBoard(board)
                print(f"Congratulations! {PLAYER_NAME_2}, you won the game!")
                Win = True
                
            # Tie Check
            elif checkFullBoard(board):
                displayBoard(board)
                print('Congratulations to both players! It\'s a TIE!')
                Tie = True
            PLAYER_TURN = 'Player 1'

    
    gameOn = playAgain()
    
print("Goodbye! Thank you for playing!")
# ===========================================================================================
