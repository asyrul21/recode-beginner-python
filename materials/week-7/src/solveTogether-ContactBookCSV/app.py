# do not delete the code in here ##############################
from helper.CsvReadWriter import CsvReadWriter
from helper.TableDisplay import TableDisplay
from helper.NavigationDisplay import NavigationDisplay

# do not delete the code in here ##############################
DATA_PATH_CSV = "data/contactList.csv"

# load data
...

# create display instance
tableDisplay = TableDisplay(data[0].keys())
navDisplay = NavigationDisplay()
# do not delete the code in here ##############################

def showInvalidOrSuccess(message):
    print(message)
    input("Press any key to continue: ")

while(True):
    ...
        

navDisplay.printExit()



