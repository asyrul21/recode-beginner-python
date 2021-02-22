from helper.JsonReadWriter import JsonReadWriter
from helper.NavigationDisplay import NavigationDisplay
from helper.TableDisplay import TableDisplay
from config import DATE_FORMAT
from Birthdate import Birthdate
from datetime import date, datetime
import time

##############################################
DATA_PATH_JSON = "data/birthdays.json"

# load data
jsonRW = JsonReadWriter(DATA_PATH_JSON)
data = jsonRW.load()

DATA_FIELDS = data[0].keys()

# create display instance
tableDisplay = TableDisplay(data[0].keys())
navDisplay = NavigationDisplay()
##############################################

def printFields(fields):
    print()
    print("Fields:")
    print("--------------------------------------------")
    for item in fields:
        print(item)
    print()

def showMessage(message):
    print(message)
    input("Press any key to continue: ")

def getTodaysDateAsString():
    today = date.today()
    return today.strftime(DATE_FORMAT)

def getRecordById(dataList, dataID):
    result = {}
    for item in dataList:
        if item["ID"] == dataID:
            result = item
    return result

def checkIfValueIsValid(field, value):
    if(field == "birthdate"):
        # will raise error if invalid date
        dateObj = datetime.strptime(value, DATE_FORMAT)
        return True if dateObj else False
    else:
        return True

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
            tableDisplay.display(data)
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
        todaysDateWithoutYear = todaysDate[:-4]
        result = []
        for item in data:
            dateWithoutYear = item["birthdate"][:-4]
            if dateWithoutYear == todaysDateWithoutYear:
                result.append(item)

        tableDisplay.display(result)
        print("Date today: " + todaysDate)
        showMessage(str(len(result)) + " result(s) were found.")

    elif(userAction == 3):
        # edit record logic
        recordID = input("What is the ID of the record to update?: ")
        recordID = int(recordID)

        printFields(DATA_FIELDS)
        field = input("Which field would you like to update?: ")

        if(field not in DATA_FIELDS):
            showMessage("Invalid field")
        else:
            newValue = input("What is the new value?: ")

            dataItem = getRecordById(data, recordID)
            valid = False
            if(dataItem == {}):
                showMessage("No record with such ID.")
            else:
                try:
                    valid = checkIfValueIsValid(field, newValue)
                except:
                    print()
                    print("Something went wrong!")
                    showMessage("Please make sure you entered a valid date format.")

                if(valid):
                    dataItem[field] = newValue
                    data[recordID - 1] = dataItem

                    jsonRW.save(data)
                    tableDisplay.display(data)
                    showMessage("Updated successfully.")

    elif(userAction == 4):
        # delete record
        # edit record logic
        recordID = input("What is the ID of the record to delete?: ")
        recordID = int(recordID)

        confirm = input("Are you sure you want to delete " + data[recordID - 1]["name"] + "'s birthdate record? (Y/N): ")

        if(confirm == "Y" or confirm == "y"):
            updatedData = [item for item in data if item["ID"] != recordID]

            data = updatedData
            jsonRW.save(data)
            tableDisplay.display(data)
            showMessage("Deleted successfully.")
        else:
            showMessage("Delete cancelled.")

    elif(userAction == 5):
        # search item by name
        name = input("Insert name to search for: ")

        searchResults = []
        for item in data:
            if name.lower() in item["name"].lower():
                searchResults.append(item)

        tableDisplay.display(searchResults)
        showMessage(str(len(searchResults)) + " result(s) found.")

    elif(userAction == 6):
        break

    else:
        print("Invalid Input!")
        

navDisplay.printExit()
