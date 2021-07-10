###############################################################
# do not modify the code in here ##############################
from helper.JsonReadWriter import JsonReadWriter
from helper.TableDisplay import TableDisplay
from helper.NavigationDisplay import NavigationDisplay

DATA_PATH_JSON = "data/patients.json"

# load data
jsonRW = JsonReadWriter(DATA_PATH_JSON)
data = jsonRW.load()

DATA_FIELDS = list(data[0].keys())

# create display instance
tableDisplay = TableDisplay(DATA_FIELDS)
navDisplay = NavigationDisplay()
# do not delete the code in here ##############################
###############################################################
# 1. Open the data file patients.json in the data folder. Observe the keys of each data item
# 2. Create a Patient class, defining a constructor and initialising the instance variables.
# In the constructor, you need to use the EXACT field names as you saw in step 1.
# 3. Observe the functionalities available in the NavigationDisplay class's displaymainMenu method
# 4. Use input to get user action and cast it to integer.
# 5. Use if statements to handle multiple functionalities. For example, if user inputs 1, you should write code
# to handle adding new data.
# 6. To display the table with data, use tableDisplay.display(data)
# 7. To save data to JSON file, use jsonRW.save(data)
# 8. To add new entry to the data variable, append it with the Dictionary form of the Patient class instance
# 9. This is a fairly open-ended coding challenge. Time to put that Creative mind to good use. Happy coding!


class Patient:
    def __init__(self, ID, fullName, birthdate, contact, lastVisitDate, lastVisitDescription):
        self.ID = ID
        self.fullName = fullName
        self.birthdate = birthdate
        self.contact = contact
        self.lastVisitDate = lastVisitDate
        self.lastVisitDescription = lastVisitDescription


def printFields():
    print()
    print("Fields:")
    print("--------------------------------------------")
    for item in DATA_FIELDS[1:]:
        print(item)
    print()

def getRecordById(dataList, dataID):
    result = {}
    for item in dataList:
        if item["ID"] == dataID:
            result = item
    return result

def showInvalidOrSuccess(message):
    print(message)
    input("Press any key to continue: ")

def generateDataID():
    ListOfIDs = [int(item["ID"]) for item in data]
    maxId = max(ListOfIDs)
    return maxId + 1

while(True):
    tableDisplay.display(data)
    navDisplay.printMainMenu()

    userAction = input("What would you like to do? : ")
    userAction = int(userAction)

    if(userAction == 1):
        tableDisplay.display(data)

        # get info
        ID = generateDataID()
        fullName = input("What is the full name of the new patient?: ")
        birthdate = input("What is the patient's birthdate? (DD/MM/YYYY)?: ")
        contact = input("What is the patient's contact number?: ")
        lastVisitDate = input("When was the patient's last visit? (DD/MM/YYYY): ")
        lastVisitDescription = input("What happened in the last visit?: ")

        newPatient = Patient(ID, fullName, birthdate, contact, lastVisitDate, lastVisitDescription)

        data.append(newPatient.__dict__)
        jsonRW.save(data)

        tableDisplay.display(data)
        showInvalidOrSuccess("Added new record with ID " + str(ID))

    elif(userAction == 2):
        name = input("Insert name to search for: ")

        searchResults = []
        for item in data:
            print(item)
            if name.lower() in item["fullName"].lower():
                searchResults.append(item)

        tableDisplay.display(searchResults)
        showInvalidOrSuccess(str(len(searchResults)) + " result(s) found.")

    elif(userAction == 3):
        # edit record logic
        recordID = input("What is the ID of the record?: ")
        recordID = int(recordID)

        dataItem = getRecordById(data, recordID)
        if(dataItem == {}):
            showInvalidOrSuccess("No record with such ID.")
        else:
            printFields()
            field = input("Which field would you like to update?: ")

            if(field not in DATA_FIELDS):
                showInvalidOrSuccess("Invalid field")
            else:
                newValue = input("What is the new value?: ")
                dataItem[field] = newValue
                data[recordID - 1] = dataItem

                jsonRW.save(data)
                tableDisplay.display(data)
                showInvalidOrSuccess("Updated successfully.")

    elif(userAction == 4):
        break

    else:
        print("Invalid Input!")
        

navDisplay.printExit()



