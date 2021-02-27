from helper.CsvReadWriter import CsvReadWriter
from helper.JsonReadWriter import JsonReadWriter
from helper.NavigationDisplay import NavigationDisplay
from helper.TableDisplay import TableDisplay
import random
import time
from helper.Utility import clearScreen


##############################################
SYMBOLS = ["'", "/", "\\", "?", "."]
DATA_PATH_CSV_QUESTIONS = "data/questions.csv"
DATA_PATH_JSON_SCOREBOARD = "data/scoreBoard.json"

# load data
jsonRW = JsonReadWriter(DATA_PATH_JSON_SCOREBOARD)
scoreBoardData = jsonRW.load()

csvRW = CsvReadWriter(DATA_PATH_CSV_QUESTIONS)
questionsData = csvRW.loadAsDictionary()

SCOREBOARD_FIELDS = scoreBoardData[0].keys()

# this is to sort items in a list
# To sort the list in place...
# ut.sort(key=lambda x: x.count, reverse=True)
# # To return a new list, use the sorted() built-in function...
# newlist = sorted(ut, key=lambda x: x.count, reverse=True)
# https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects

scoreBoardData.sort(key=lambda x: x["score"], reverse=True)
highestScore = scoreBoardData[0]["score"]

# create display instance
tableDisplay = TableDisplay(scoreBoardData[0].keys())
navDisplay = NavigationDisplay()
##############################################

def runCountdown():
    print()
    for i in range(0, 4):
        print(str(4-i) + "...")
        time.sleep(1)

def removeSpaceSymbolsAndLower(ans):
    result = ""
    result = ans.replace(" ", "")

    for char in result:
        if char in SYMBOLS:
            result.replace(char, "")

    return result.lower()


def showMessage(message):
    print(message)
    input("Press enter to continue: ")

def seedQuestions(data):
    questions = []
    # 10 questions
    for i in range(0, 10):
        question = random.choice(data)
        while(question in questions):
            question = random.choice(data)
        questions.append(question)
    return questions

def checkAnswer(actual, attempt):
    cleanedActual = removeSpaceSymbolsAndLower(actual).strip()
    cleanedAttempt = removeSpaceSymbolsAndLower(attempt).strip()
    if(attempt == ""):
        return False
    elif(cleanedActual in cleanedAttempt or cleanedAttempt in cleanedActual):
        return True
    else:
        return False

def updateScoreBoard(player):
    for item in scoreBoardData:
        if item["name"] == player["name"]:
            item["score"] = player["score"]
    scoreBoardData.sort(key=lambda x: x["score"], reverse=True)
    jsonRW.save(scoreBoardData)

def checkExistingPlayer(player):
    for item in scoreBoardData:
        if item["name"] == player["name"]:
            return True
    return False


def addScoreToData(player):
    playerAlreadyExits = checkExistingPlayer(player)

    if(playerAlreadyExits):
        updateScoreBoard(player)
    else:
        scoreBoardData.append(player)
        scoreBoardData.sort(key=lambda x: x["score"], reverse=True)
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
                playerScore += 1000
                navDisplay.displayQuestionAndScore(question, playerScore, answer)
                showMessage("CORRECT!")
            else:
                navDisplay.displayQuestionAndScore(question, playerScore, answer)
                showMessage("WRONG.")


        navDisplay.displayQuestionAndScore(question, playerScore)
        print("\tFinish!")
        showMessage("Your total score: " + str(playerScore))

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

# main
while(True):
    clearScreen()
    print("\tWelcome to the Ultimate Trivia!")
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
        print("Invalid input!")

navDisplay.printExit()




