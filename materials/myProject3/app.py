from helper.CsvReadWriter import CsvReadWriter
from helper.NavigationDisplay import NavigationDisplay
from helper.TableDisplay import TableDisplay
from helper.Utility import clearScreen
from InventoryItem import InventoryItem

####################

csvRW = CsvReadWriter("data/inventory.csv")
data = csvRW.loadAsDictionary()

DATA_FIELDS = list(data[0].keys())

navDisplay = NavigationDisplay()
tableDisplay = TableDisplay(DATA_FIELDS)

####################

def showMessage(message):
    print(message)
    input("Press enter to continue: ")

def generateDataID():
    listOfIDs = [ int(item["ID"]) for item in data ]
    maxId = max(listOfIDs)
    return maxId + 1

def printFields():
    print()
    print("Fields:")
    print("--------------------------------------------")
    for item in DATA_FIELDS[1:]:
        print(item)
    print()

while(True):
    navDisplay.printMainMenu()
    try:
        userAction = input("What would you like to do?: ")
        userAction = int(userAction)

        if(userAction == 1):
            # display
            tableDisplay.display(data)
            print()
            showMessage(str(len(data)) + " item(s) stored.")

        elif(userAction == 2):
            # create data
            ID = generateDataID()
            name = input("Insert the name of the item: ")
            category = input("How would you like to categorise this item? : ")
            quantity = input("How many of these items are there in stock? : ")
            description = input("Add a short description: ")

            # itemEntry = InventoryItem(ID, name, category, quantity, description)

            itemEntry = {
                "ID": ID,
                "Item" : name,
                "Category": category,
                "Quantity": quantity,
                "Description": description
            }
            
            data.append(itemEntry)
            csvRW.save(data)

            showMessage("New item successfully added.")

        elif(userAction == 3):
            # update data
            tableDisplay.display(data)
            print()

            recordID = input("What is the ID of the item you want to update? : ")

            printFields()
            field = input("Which of the above fields would you like to update? : ")

            if(field not in DATA_FIELDS[1:]):
                showMessage("Invalid field.")
            else:
                newValue = input("What is the new value? : ")

                for item in data:
                    if item["ID"] == recordID:
                        item[field] = newValue
                        break
                
                csvRW.save(data)
                tableDisplay.display(data)
                showMessage("Item has been updated")

        elif(userAction == 4):
            # delete data
            tableDisplay.display(data)
            print()

            recordID = input("What is the ID of the item you want to delete? : ")

            updatedData = [ item for item in data if item["ID"] != recordID ]
            data = updatedData
            csvRW.save(data)

            tableDisplay.display(data)
            showMessage("Item has been removed.")

        elif(userAction == 5):
            # search by name
            itemName = input("What is the name of the item to search for? : ")

            searchResult = []
            for item in data:
                if itemName.lower() in item["Item"].lower():
                    searchResult.append(item)

            tableDisplay.display(searchResult)
            showMessage(str(len(searchResult)) + " result(s) found.")

        elif(userAction == 6):
            # search by category
            categoryName = input("What is the name of the category to search for? : ")

            searchResult = []
            for item in data:
                if categoryName.lower() in item["Category"].lower():
                    searchResult.append(item)

            tableDisplay.display(searchResult)
            showMessage(str(len(searchResult)) + " result(s) found.")

        elif(userAction == 7):
            break
        else:
            showMessage("Invalid user action!")
    except Exception as err:
        showMessage("Invalid user action!")


navDisplay.printExit()

