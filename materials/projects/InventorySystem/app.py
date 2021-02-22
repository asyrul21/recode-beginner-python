from helper.CsvReadWriter import CsvReadWriter
from helper.NavigationDisplay import NavigationDisplay
from helper.TableDisplay import TableDisplay
from InventoryItem import InventoryItem

##############################################
DATA_PATH = "data/inventory.csv"

# load data
csvRW = CsvReadWriter(DATA_PATH)
data = csvRW.loadAsDictionary()

DATA_FIELDS = list(data[0].keys())

# create display instance
tableDisplay = TableDisplay(data[0].keys())
navDisplay = NavigationDisplay()
##############################################

def showMessage(message):
    print(message)
    input("Press enter to continue: ")

def printFields():
    print()
    print("Fields:")
    print("--------------------------------------------")
    for item in DATA_FIELDS[1:]:
        print(item)
    print()

def generateCategoryList():
    result = []
    for item in data:
        if item["Category"] not in result:
            result.append(item["Category"])
    return result

def printCategories():
    cats = generateCategoryList()
    print()
    print("Fields:")
    print("--------------------------------------------")
    for item in cats:
        print(item)
    print()

def getRecordById(dataID):
    result = {}
    for item in data:
        if item["ID"] == dataID:
            result = item
    return result

def generateDataID():
    ListOfIDs = [int(item["ID"]) for item in data]
    maxId = max(ListOfIDs)
    return maxId + 1

# main
while(True):
    navDisplay.printMainMenu()
    userAction = input("What would you like to do?: ")
    userAction = int(userAction)

    if(userAction == 1):
        # display table if items
        tableDisplay.display(data)
        print()
        showMessage(str(len(data)) + " item(s) found.")

    elif(userAction == 2):
        # create item
        # ID = len(data) + 1
        ID = generateDataID()
        name = input("What is the item?: ")
        category = input("How would you categorise this item?: ")
        quantity = input("How many of these items are available?: ")
        desc = input("Add a short description: ")

        newItem = InventoryItem(ID, name, category, quantity, desc)

        data.append(newItem.dictionaryForm)
        csvRW.save(data)
        showMessage("New entry of ID " + str(ID) + " has been added.")

    elif(userAction == 3):
        # edit item
        tableDisplay.display(data)
        print()

        recordID = input("What is the ID of the item to update?: ")

        # in csv's, data are all string by default
        # dont need to casr
        # recordID = int(recordID)

        dataItem = getRecordById(recordID)
        if(dataItem == {}):
            showMessage("No record with such ID.")
        else:
            printFields()
            field = input("Which field would you like to update?: ")
            if(field not in DATA_FIELDS):
                showMessage("Invalid field.")
            else:
                newValue = input("What is the new value?: ")
                dataItem[field] = newValue
                data[int(recordID) - 1] = dataItem

                csvRW.save(data)
                tableDisplay.display(data)
                showMessage("Updated successfully.")

    elif(userAction == 4):
        #delete
        # edit item
        tableDisplay.display(data)
        print()

        recordID = input("What is the ID of the item to delete?: ")
        dataItem = getRecordById(recordID)
        if(dataItem == {}):
            showMessage("No record with such ID.")
        else:
            confirm = input("Are you sure you want to delete item with ID " + recordID + "? (Y/N): ")
            if(confirm == "Y" or confirm == "y"):
                updatedData = [item for item in data if item["ID"] != recordID]
                data = updatedData
                csvRW.save(data)
                tableDisplay.display(data)
                showMessage("Deleted successfully.")
            else:
                showMessage("Delete cancelled.")

    elif(userAction == 5):
        # search item by name
        itemName = input("Insert item to search for: ")

        searchResults = []
        for item in data:
            if itemName.lower() in item["Item"].lower():
                searchResults.append(item)

        tableDisplay.display(searchResults)
        showMessage(str(len(searchResults)) + " result(s) found.")

    elif(userAction == 6):
         # search item by category
        printCategories()
        category = input("Insert category to search for: ")

        searchResults = []
        for item in data:
            if category.lower() in item["Category"].lower():
                searchResults.append(item)

        tableDisplay.display(searchResults)
        showMessage(str(len(searchResults)) + " result(s) found.")

    elif(userAction == 7):
        break

    else:
        print("Invalid Input!")

navDisplay.printExit()