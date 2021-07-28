# For this endOFClass exercise, we will simulate an activity tracker of 3 employees
# The first part of this exercise is to define an employee class
# The employee class has the attributes name, position, department, and working
# the working property has a default value of False
# An employee also has methods called startWork() and finishWork()
# if the value of time is 9, each employee will execute their startWork() method
# this method than changes their instance variable `working` to True
# if the value of time is 18, each employee will execute their finishWork() method
# this will then change the variable `working` back to false
# The revealActivity method shows what the instance is doing given the time of day


import time
import os

# Create employee class
# do not change this part
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.working = False

    def startWork(self):
        print(self.name + " goes to work!")
        self.working = True

    def finishWork(self):
        print("Time for " + self.name + " to go home!")
        self.working = False

    def revealActivity(self):
        if(self.working):
            print(self.name + " is working!")
        else:
            print(self.name + " is resting......")


########### COMPLETE THIS PART #############
# create 3 instances
employee1 = Employee("Ahmad", "Engineer")
employee2 = Employee("Siti", "Quality Assurance")
employee3 = Employee("Bob", "Manager")

# store these in list
employees = [employee1, employee2, employee3]
############################################


################# methods ##################
# DO NOT CHANGE THIS CODE
def startWorkForAllEmployees():
    for e in employees:
        e.startWork()

def endWorkForAllEmployees():
    for e in employees:
        e.finishWork()

def revealActivityForAllEmployees():
    for e in employees:
        e.revealActivity()
################# methods ##################


# DO NOT CHANGE THE CODE BELOW
dayTime = range(6, 19)
os.system("clear")
for hour in dayTime:
    print()
    print('============================')
    print("Time: " + str(hour) + ":00")
    print()
    print("Activity:")
    print('----------------------------')
    if(hour == 9):
        startWorkForAllEmployees()
        print()
    elif(hour == 18):
        endWorkForAllEmployees()
        print()

    revealActivityForAllEmployees()    
    
    time.sleep(2)