from helper.JsonReadWriter import JsonReadWriter
from helper.NavigationDisplay import NavigationDisplay
from helper.TableDisplay import TableDisplay
from Birthdate import Birthdate
from datetime import date
import time


##############################################
DATA_PATH_JSON = "data/birthdays.json"
DATE_FORMAT = "%d/%m/%Y"

# load data
jsonRW = JsonReadWriter(DATA_PATH_JSON)
data = jsonRW.load()

# create display instance
tableDisplay = TableDisplay(data[0].keys())
navDisplay = NavigationDisplay()
##############################################

def showMessage(message):
    print(message)
    input("Press any key to continue: ")

def getTodaysDateAsString():
    today = date.today()
    return today.strftime(DATE_FORMAT)

print("Welcome to the Birthdate Tracker!")
print()
while(True):
    tableDisplay.display(data)
    navDisplay.printMainMenu()

    userAction = input("What would you like to do? : ")
    userAction = int(userAction)

    if(userAction == 1):
        try:
            ID = len(data) + 1
            name = input("Insert name: ")
            relation = input("What is the relationship of this person to you?: ")
            birthdate = input("Type the birthdate in the format of DD/MM/YYYY: ")

            # if user keys in invalid date this will raise exception         
            entry = Birthdate(ID, name, relation, birthdate)

            data.append(entry.getDictionaryForm())
            jsonRW.save(data)

            print()
            showMessage("New entry of ID " + str(ID) + " has been added.")
        except:
            print()
            print("Something went wrong!")
            showMessage("Please make sure you entered a valid date format.")

    elif(userAction == 2):
        print()
        print("Processing...")
        time.sleep(1)

        todaysDate = getTodaysDateAsString()
        result = []
        for item in data:
            if item["birthdate"] == todaysDate:
                result.append(item)

        tableDisplay.display(result)
        showMessage(str(len(result)) + " result(s) were found.")

    elif(userAction == 3):
        break

    else:
        print("Invalid Input!")
        

navDisplay.printExit()