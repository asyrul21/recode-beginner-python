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
        ...

    elif(userAction == 2):
        ...

    elif(userAction == 3):
        break

    else:
        print("Invalid Input!")
        

navDisplay.printExit()



