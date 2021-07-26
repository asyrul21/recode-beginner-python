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
        try:
            eventDate = input("Type in the memorable date in the format of DD/MM/YYYY: ")
            event = input("What happened on this date?: ")
            dateObj = datetime.strptime(eventDate, DATE_FORMAT)

            newEvent = {
                "ID": generateDataID(),
                "event": event,
                "date": eventDate
            }

            data.append(newEvent)
            jsonRW.save(data)

            print()
            tableDisplay.display(data)
            showMessage("New memorable date has been added.")
        except Exception as err:
            print()
            print("Something went wrong")
            showMessage("Please make sure that your date is valid.")

    elif(userAction == 2):
        print()
        print("Processing...")
        time.sleep(1)

        todaysDate = getTodaysDateAsString()
        todaysDateWithoutYear = todaysDate[:-4]
        result = []
        for item in data:
            dateWithoutYear = item["date"][:-4]
            if dateWithoutYear == todaysDateWithoutYear:
                result.append(item)

        tableDisplay.display(result)
        print("Date today: " + todaysDate)
        showMessage(str(len(result)) + " result(s) were found.")

    elif(userAction == 3):
        # delete record
        # edit record logic
        recordID = input("What is the ID of the date to delete?: ")
        recordID = int(recordID)

        confirm = input("Are you sure you want to delete " + data[recordID - 1]["event"] + "'s memorable date? (Y/N): ")

        if(confirm == "Y" or confirm == "y"):
            updatedData = [item for item in data if item["ID"] != recordID]

            data = updatedData
            jsonRW.save(data)
            tableDisplay.display(data)
            showMessage("Deleted successfully.")
        else:
            showMessage("Delete cancelled.")

    elif(userAction == 4):
        # search item by name
        name = input("Insert event to search for: ")

        searchResults = []
        for item in data:
            if name.lower() in item["event"].lower():
                searchResults.append(item)

        tableDisplay.display(searchResults)
        showMessage(str(len(searchResults)) + " result(s) found.")

    elif(userAction == 5):
        break

    else:
        print("Invalid Input!")
        

navDisplay.printExit()
