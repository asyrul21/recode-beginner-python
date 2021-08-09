from helper.JsonReadWriter import JsonReadWriter
from helper.NavigationDisplay import NavigationDisplay
from helper.TableDisplay import TableDisplay
from helper.Utility import clearScreen
from Birthdate import Birthdate
from datetime import date, datetime
from config import DATE_FORMAT
import time

##############################

jsonRW = JsonReadWriter("data/birthdays.json")
data = jsonRW.load()

DATA_FIELDS = list(data[0].keys())

tableDisplay = TableDisplay(data[0].keys())
navDisplay = NavigationDisplay()

##############################

def showMessage(message):
    print(message)
    input("Press any key to continue: ")

def generateDataID():
    listOfIDs = [ int(item["ID"]) for item in data]
    maxID = max(listOfIDs)
    return maxID + 1

def getItemById(recordID):
    for item in data:
        if item["ID"] == recordID:
            return item

def getTodaysDateAsString():
    today = date.today()
    return today.strftime(DATE_FORMAT)

def printFields():
    print()
    print("Fields:")
    print("--------------------------------------------")
    for item in DATA_FIELDS[1:]:
        print(item)
    print() 

print("Welcome to the Birthday Tracker!")
print()
while(True):
    tableDisplay.display(data)
    navDisplay.printMainMenu()

    userAction = input("What would you like to do? : ")
    userAction = int(userAction)

    if(userAction == 1):
        try:
            ID = generateDataID()
            name = input("Insert name: ")
            relation = input("What is the relationship of this person to you? ")
            birthdate = input("Insert the birthdate in the format of DD/MM/YYYY: ")

            entry = Birthdate(ID ,name, relation, birthdate)

            data.append(entry.getDictionaryForm())
            jsonRW.save(data)

            print()
            tableDisplay.display(data)
            showMessage("New birthdate record has been added!")
        except:
            print()
            print("Something went wrong")
            showMessage("Please make sure you entered a valid date format")

    elif(userAction == 2):
        print()
        print("Processing...")
        time.sleep(1)

        todaysDate = getTodaysDateAsString()
        todaysDateWithoutYear = todaysDate[:-4]

        result = []
        for item in data:
            dateWithoutYear = item["birthdate"][:-4]
            if(dateWithoutYear == todaysDateWithoutYear):
                result.append(item)

        tableDisplay.display(result)
        print("Date today: " + todaysDate)
        showMessage(str(len(result)) + " ressult(s) were found.")

    elif(userAction == 3):
        recordID = input("What is the ID of the record to update?: ")
        recordID = int(recordID)

        dataItem = getItemById(recordID)

        printFields()
        field = input("Which field would you like to update? ")
        newValue = input("What is the new value? : ")

        for item in data:
            if(item["ID"] == recordID):
                item[field] = newValue
                break

        jsonRW.save(data)
        tableDisplay.display(data)
        showMessage("Updated successfully!")

    elif(userAction == 4):
        recordID = input("What is the ID of the record to delete?: ")
        recordID = int(recordID)

        updatedData = [item for item in data if item["ID"] != recordID]
        data = updatedData
        jsonRW.save(data)
        tableDisplay.display(data)
        showMessage("Birthdate deleted.")

    elif(userAction == 5):
        name = input("What is the name to search for: ")

        searchResults = []
        for item in data:
            if name.lower() in item["name"].lower():
                searchResults.append(item)

        tableDisplay.display(searchResults)
        showMessage(str(len(searchResults)) + " result(s) found.")

    elif(userAction == 6):
        break

navDisplay.printExit()
    