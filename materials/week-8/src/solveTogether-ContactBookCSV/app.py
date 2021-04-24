# do not delete the code in here ##############################
from helper.CsvReadWriter import CsvReadWriter
from helper.TableDisplay import TableDisplay
from helper.NavigationDisplay import NavigationDisplay

# do not delete the code in here ##############################
DATA_PATH_CSV = "data/contactList.csv"

# load data
csvRW = CsvReadWriter(DATA_PATH_CSV)
data = csvRW.loadAsDictionary()

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

    userAction = input("What would you like to do? : ")
    userAction = int(userAction)

    if(userAction == 1):
        tableDisplay.display(data)

        name = input("What is the name of the new contact? ")
        relation = input("What is the relation of the contact? ")
        home = input("What is the home number? ")
        mobile = input("What is the mobile number? ")

        newContact = {
            "name": name,
            "relation": relation,
            "home": home,
            "mobile": mobile
        }

        data.append(newContact)
        csvRW.save(data)

        tableDisplay.display(data)
        showInvalidOrSuccess("New contact added!")

    elif(userAction == 2):
        name = input("Insert name to search for: ")

        searchResults = []
        for item in data:
            if(name.lower() in item["name"].lower()):
                searchResults.append(item)

        tableDisplay.display(searchResults)
        showInvalidOrSuccess(str(len(searchResults)) + " result(s) found.")

    elif(userAction == 3):
        break

    else:
        showInvalidOrSuccess("Invalid Input!")
        

navDisplay.printExit()



