from helper.JsonReadWriter import JsonReadWriter
from helper.NavigationDisplay import NavigationDisplay
from helper.TableDisplay import TableDisplay
from datetime import date, datetime
import time

##############################################
DATE_FORMAT="%d/%m/%Y"
DATA_PATH_JSON = "data/dates.json"

# load data
jsonRW = JsonReadWriter(DATA_PATH_JSON)
data = jsonRW.load()

DATA_FIELDS = list(data[0].keys())

# create display instance
tableDisplay = TableDisplay(data[0].keys())
navDisplay = NavigationDisplay()
##############################################

def printFields():
    print()
    print("Fields:")
    print("--------------------------------------------")
    for item in DATA_FIELDS[1:]:
        print(item)
    print()

def showMessage(message):
    print(message)
    input("Press any key to continue: ")

def getTodaysDateAsString():
    today = date.today()
    # convert to string
    return today.strftime(DATE_FORMAT)

def generateDataID():
    ListOfIDs = [int(item["ID"]) for item in data]
    maxId = max(ListOfIDs)
    return maxId + 1

print("Welcome to the Memorable Date App!")
print()
while(True):
    tableDisplay.display(data)
    navDisplay.printMainMenu()

    userAction = input("What would you like to do? : ")
    userAction = int(userAction)

    if(userAction == 1):
        ...

    elif(userAction == 2):
        ...

    elif(userAction == 3):
        ...

    elif(userAction == 4):
        ...

    elif(userAction == 5):
        break

    else:
        print("Invalid Input!")
        

navDisplay.printExit()
