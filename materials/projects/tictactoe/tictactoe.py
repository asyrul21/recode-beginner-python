from helper.Utility import clearScreen

clearScreen()
print("Welcome to the tic tac toe game!")


def generateGameBoard():
    board = [
                [0, 1, 2], 
                [0, 1, 2], 
                [0, 1, 2]
            ]
    return board

def initialize(board):
    for i in range(0, 3):
        for j in range(0, 3):
            board[i][j] = ""
    return board    

def getInputLocation(playerInput):
    if(playerInput == "tl"):
        return [0, 0]
    elif(playerInput == "tm"):
        return [0,1]
    elif(playerInput == "tr"):
        return [0,2]
    elif(playerInput == "ml"):
        return [1,0]
    elif(playerInput == "mm"):
        return [1,1]
    elif(playerInput == "mr"):
        return [1,2]
    elif(playerInput == "bl"):
        return [2,0]
    elif(playerInput == "bm"):
        return [2,1]
    elif(playerInput == "br"):
        return [2,2]
    else:
        raise Exception("Invalid Input!")

def checkIfInputAlreadyOccupied(board, playerInput):
    boardLocation = getInputLocation(playerInput)
    return board[boardLocation[0]][boardLocation[1]] == ""

def updateBoard(board, playerInput, symbol):
    boardLocation = getInputLocation(playerInput)
    board[boardLocation[0]][boardLocation[1]] = symbol

def checkPlayerWon(board, symbol):
    # horizontals
    if(board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol): return True
    elif(board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol): return True
    elif(board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol): return True
    # verticals
    elif(board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol): return True
    elif(board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol): return True
    elif(board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol): return True
    # diagonals
    elif(board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol): return True
    elif(board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol): return True
    else: return False

def displayBoard(board):
    for i in range(0, 3):
        if(i != 0):
            print("=================================================")
        print("\t \t||\t \t||\t \t")
        horizontalString = ""
        for j in range(0,3):
            if(j == 0 or j == 1):
                horizontalString = horizontalString + "\t" + str(board[i][j]) + "\t||"
            else:
                horizontalString = horizontalString + "\t" + str(board[i][j])
        print(horizontalString)
        print("\t \t||\t \t||\t \t")

                

def display(board, p1Score, p2Score, round):
    clearScreen()
    print("--------------------------------------------------")
    print("\t\t      Round: " + str(round))
    print("--------------------------------------------------")
    print()
    displayBoard(board)
    print()
    print("--------------------------------------------------")
    print("\t\t      Score")
    print("--------------------------------------------------")
    print("Player 1: " + str(p1Score) + "\t\tPlayer 2: " + str(p2Score))
    print("==================================================")
    print()
    
def askForInput():
    print("\t\t      Controls:")
    print("Top Right \t=> tr, Top Middle \t=> tm, Top Left \t=> tl")
    print("Middle Right \t=> mr, Middle Middle \t=> mm, Middle Left \t=> ml")
    print("Bottom Right \t=> br, Bottom Middle \t=> bm, Bottom Left \t=> bl")
    print()
    userInput = input("Insert your move: ")
    return userInput

repeat = True
while(repeat):
    print()
    rounds = input("How many rounds would you like to play? (1, 3, 5): ")
    rounds = int(rounds)
    counter = 0
    p1Score = 0
    p2Score = 0
    while(counter < rounds):
        # create and initialise game board
        gameBoard = generateGameBoard()
        gameBoard = initialize(gameBoard)

        # setup boolean
        firstPlayer = True
        playerWon = False
        winner = ""
        while(not playerWon):
            display(gameBoard, p1Score, p2Score, counter + 1)
            playerSymbol = "X" if firstPlayer else "O"

            if(firstPlayer):
                print("Player 1's turn (X)")
            else:
                print("Player 2's turn (O)")

            print("--------------------")
            print()
            playerInput = askForInput()
            print()

            updateReady = checkIfInputAlreadyOccupied(gameBoard, playerInput)
            if(updateReady):
                updateBoard(gameBoard, playerInput, playerSymbol)

                # check if player wins
                playerWon = checkPlayerWon(gameBoard, playerSymbol)

                if(playerWon):
                    winner = "Player 1" if firstPlayer else "Player 2"
                    if(firstPlayer):
                        p1Score += 1
                    else:
                        p2Score += 1

                    print()
                    display(gameBoard, p1Score, p2Score, counter + 1)
                    counter = counter + 1
                    print(winner + " won this round!")
                    print()
                    proceed = input("Type any key to continue ")
                else:
                    # flip player turn
                    firstPlayer = not firstPlayer
            else:
                print("That position is already occupied!")
                print("Please choose a new location.")

    display(gameBoard, p1Score, p2Score, counter + 1)
    ultimateWinner = "Player 1" if p1Score > p2Score else "Player 2"
    print()
    print("Congratulations! " + ultimateWinner + " won overall!")
    print()
    ans = input("Play another round? (Y/N): ")
    repeat = False if ans == "N" or ans == "n" else True

clearScreen()
print("Goodbye!")
