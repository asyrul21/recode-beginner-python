from helper.CsvReadWriter import CsvReadWriter
from helper.JsonReadWriter import JsonReadWriter
from helper.NavigationDisplay import NavigationDisplay
from helper.TableDisplay import TableDisplay
from helper.Utility import clearScreen
import random
import time

###################################
SYMBOLS = ["'", "/", "\\", "?", "."]
DATA_PATH_CSV_QUESTIONS = "data/questions.csv"
DATA_PATH_JSON_SCOREBOARD = "data/scoreBoard.json"

jsonRW = JsonReadWriter(DATA_PATH_JSON_SCOREBOARD)
scoreBoardData = jsonRW.load()

csvRW = CsvReadWriter(DATA_PATH_CSV_QUESTIONS)
questionsData = csvRW.loadAsDictionary()

SCOREBOARD_FIELDS = scoreBoardData[0].keys()
tableDisplay = TableDisplay(SCOREBOARD_FIELDS)

scoreBoardData.sort(key= lambda x: x["score"], reverse = True)
highestScore = scoreBoardData[0]["score"]

navDisplay = NavigationDisplay()
####################################

def showMessage(message):
    print(message)
    input("Press enter to continue: ")

def seedQuestions(data):
    questions = []
    for i in range(0,10):
        question = random.choice(data)
        while(question in questions):
            question = random.choice(data)

        questions.append(question)
    return questions

def removeSpaceSymbolsAndLower(ans):
    result = ""
    result = ans.replace(" ", "")

    for char in result:
        if char in SYMBOLS:
            result.replace(char, "")

    return result.lower()

def runCountdown():
    print()
    for i in range(4, 0, -1):
        print(str(i) + "...")
        time.sleep(1)

def checkAnswer(actual, attempt):
    cleanActual = removeSpaceSymbolsAndLower(actual).strip()
    cleanAttempt = removeSpaceSymbolsAndLower(attempt).strip()

    if(attempt == ""):
        return False
    elif(cleanActual in cleanAttempt or cleanAttempt in cleanActual):
        return True
    else:
        return False

def checkExistingPlayer(playerObj):
    for item in scoreBoardData:
        if item["name"] == playerObj["name"]:
            return True
    return False

def updateScoreBoard(player):
    for item in scoreBoardData:
        if item["name"] == player["name"]:
            item["score"] = player["score"]
    scoreBoardData.sort(key= lambda x: x["score"], reverse = True)
    jsonRW.save(scoreBoardData)

def addScoreToData(newScore):
    playerAlreadyExists = checkExistingPlayer(newScore)

    if(playerAlreadyExists):
        updateScoreBoard(newScore)
    else:
        scoreBoardData.append(newScore)
        scoreBoardData.sort(key= lambda x: x["score"], reverse = True)
        jsonRW.save(scoreBoardData)


def playGame(playerName):
    repeat = True
    while(repeat):
        questions = seedQuestions(questionsData)
        playerScore = 0

        showMessage("You will be given 10 questions to answer correctly. Ready?")
        runCountdown()

        for q in questions:
            correct = False
            question = q["Question"]
            answer = q["Answer"]

            navDisplay.displayQuestionAndScore(question, playerScore)
            playerAnswer = input("Your answer: ")

            correct = checkAnswer(answer, playerAnswer)
            if(correct):
                playerScore = playerScore + 1000
                navDisplay.displayQuestionAndScore(question, playerScore, answer)
                showMessage("CORRECT!")
            else:
                navDisplay.displayQuestionAndScore(question, playerScore, answer)
                showMessage("WRONG.")

        navDisplay.displayQuestionAndScore(question, playerScore)
        print("\tFinish!")
        showMessage("Your total score is: " + str(playerScore))

        if(playerScore > highestScore):
            print()
            showMessage("CONGRATULATIONS WE HAVE A NEW HIGH SCORE!")
        
        print()
        ans = input("Retry? (Y/N): ")
        repeat = False if ans == "n" or ans == "N" else True
    
    playerObj = {
        "name": playerName,
        "score": playerScore
    }
    addScoreToData(playerObj)


while(True):
    clearScreen()
    print("\tWelcome to the Quiz Game!")
    print()
    navDisplay.printMainMenu()

    userAction = input("What would you like to do? ")
    userAction = int(userAction)

    if(userAction == 1):
        name = input("Insert your name: ")
        playGame(name)
    elif(userAction == 2):
        tableDisplay.display(scoreBoardData)
        showMessage("")
    elif(userAction == 3):
        break
    else:
        showMessage("Invalid input!")


navDisplay.printExit()