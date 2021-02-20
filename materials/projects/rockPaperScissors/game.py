import time
from helper.NavigationDisplay import NavigationDisplay

def getIntInput(message):
    result = input(message)
    return int(result)

def runCountdown():
    print()
    for i in range(0, 5):
        print(str(5-i) + "...")
        time.sleep(1)

def getCurrentPlayer(playerBool):
    return "Player 1" if playerBool else "Player 2"

def getPlayerMove(player):
    print()
    print(player + "'s Turn")
    move = input("Please select your move (make sure your opponent isn't looking!): ")
    return int(move)

def computeWinner(moves):
    player1 = moves[0]
    player2 = moves[1]
    rock = 1
    paper = 2
    scissors = 3
    
    # for rock
    if(player1 == 1 and player2 == 2):
        return 1
    elif(player1 == 1 and player2 == 3):
        return 0
    # for paper
    elif(player1 == 2 and player2 == 1):
        return 0
    elif(player1 == 2 and player2 == 3):
        return 1
    # for scissors
    elif(player1 == 3 and player2 == 1):
        return 1
    elif(player1 == 3 and player2 == 2):
        return 0
    elif(player1 == player2):
        return -1


def printMessage(message):
    print()
    print(message)
    input("Press and key to proceed ")

def getMoveFromId(id):
    if id == 1:
        return "Rock"
    elif id == 2:
        return "Paper"
    else:
        return "Scissors"

def printMoves(p1move, p2move):
    print("Player 1 chose: " + getMoveFromId(p1move))
    print("player 2 chose: " + getMoveFromId(p2move))


navDisplay = NavigationDisplay()
    

print("Welcome to the Rock Paper Scissors Game!")
print()
rounds = getIntInput("How many rounds would you like to play? ")
print()
print("Player 1 moves first, make sure your opponent isn't looking.")
print("Ready?")
runCountdown()


repeat = True
while(repeat):
    roundCounter = 0
    player1score = 0
    player2score = 0
    while(rounds - roundCounter > 0):
        navDisplay.displayHUD(player1score, player2score, roundCounter + 1)

        player1turn = True
        currentPlayer = getCurrentPlayer(player1turn)
        player1move = getPlayerMove(currentPlayer)

        player1turn = not player1turn
        currentPlayer = getCurrentPlayer(player1turn)
        navDisplay.displayHUD(player1score, player2score, roundCounter + 1)
        player2move = getPlayerMove(currentPlayer)

        moveSet = [player1move, player2move]
        navDisplay.displayHUD(player1score, player2score, roundCounter + 1)
        winnerIndex = computeWinner(moveSet)

        if winnerIndex == 0:
            player1score += 1
            navDisplay.displayHUD(player1score, player2score, roundCounter + 1)
            printMoves(player1move, player2move)
            printMessage("Player 1 won this round!")
        elif winnerIndex == 1:
            player2score += 1
            navDisplay.displayHUD(player1score, player2score, roundCounter + 1)
            printMoves(player1move, player2move)
            printMessage("Player 2 won this round!")
        else:
            printMoves(player1move, player2move)
            printMessage("Whoops that was a tie!")

        roundCounter += 1

    navDisplay.displayHUD(player1score, player2score, roundCounter + 1)
    if(player1score > player2score):
        print("Congratulations! Player 1 won overall!")
    elif(player1score < player2score):
        print("Congratulations! Player 2 won overall!")
    else:
        print("It's a tie!")

    res = input("Play again? (Y/N): ")
    repeat = False if res == "N" or res == "n" else True

navDisplay.printExit()

        
