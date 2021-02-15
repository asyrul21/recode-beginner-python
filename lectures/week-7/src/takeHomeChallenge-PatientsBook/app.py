###############################################################
# do not modify the code in here ##############################
from helper.JsonReadWriter import JsonReadWriter
from helper.TableDisplay import TableDisplay
from helper.NavigationDisplay import NavigationDisplay

DATA_PATH_JSON = "data/patients.json"

# load data
jsonRW = JsonReadWriter(DATA_PATH_JSON)
data = jsonRW.load()

DATA_FIELDS = data[0].keys()

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


# define your Patient class here
class Patient:
    def __init__(self, ...):
        ...

#########################################
### Define your functions here 
#########################################
# def showInvalidOrSuccess(message):
#     print(message)
#     input("Press any key to continue: ")



#########################################


### main logic
while(True):
    tableDisplay.display(data)
    navDisplay.printMainMenu()

    userAction = input("What would you like to do? : ")
    userAction = int(userAction)

    if(userAction == 1):
        # insert new data logic
        ...

    elif(userAction == 2):
        # search by name
        ...

    elif(userAction == 3):
        # edit logic here
        ...
    
    elif(userAction == 4):
        break

    else:
        print("Invalid Input!")
        

navDisplay.printExit()



