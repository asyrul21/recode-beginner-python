# do not delete the code in here ##############################
from helper.JsonReadWriter import JsonReadWriter
from helper.TableDisplay import TableDisplay
from helper.NavigationDisplay import NavigationDisplay

DATA_PATH_JSON = "data/contactList.json"

# load data
jsonRW = JsonReadWriter(DATA_PATH_JSON)
data = jsonRW.load()

# create display instance
tableDisplay = TableDisplay(data[0].keys())
navDisplay = NavigationDisplay()
# do not delete the code in here ##############################

def showInvalidOrSuccess(message):
    print(message)
    input("Press any key to continue: ")

while(True):
    tableDisplay.display(data)
    navDisplay.printMainMenu()

    userAction = input("What would you like to do?: ")
    userAction = int(userAction)

    if(userAction == 1):
        print("Creating new contact")
        name = input("What is the name of the new contact? ")
        relation = input("What is the relation of this person to you? ")
        home = input("What is the home contact number? Leave blank if there is not one: ")
        mobile = input("What is the mobile contact number? Leave black if there isn't one: ")

        newContact = {
            "name": name,
            "relation": relation,
            "home": home,
            "mobile":  mobile
        }

        data.append(newContact)
        jsonRW.save(data)

        tableDisplay.display(data)
        showInvalidOrSuccess("Added a new contact.")

    elif(userAction == 2):
        print("Search contact")

        name = input("Insert name to search for: ")

        searchResult = []
        for item in data:
            if name.lower() in item["name"].lower():
                searchResult.append(item)
            
        tableDisplay.display(searchResult)
        showInvalidOrSuccess(str(len(searchResult)) + " result(s) found.")
    else:
        break
        

navDisplay.printExit()

