import os

class NavigationDisplay:
    def __init__(self):
        ...

    def printMainMenu(self):
        print("--------------------------------------------")
        print("Activity\t\t\t| Selection")
        print("--------------------------------------------")
        print("Create new Birthdate Entry\t|\t1")
        print("See Who's Birthdays are Today\t|\t2")
        print("Edit a Birthdate Record\t\t|\t3")
        print("Delete a Birthdate Record\t|\t4")
        print("Search for Birthdate by Name\t|\t5")
        print("Exit\t\t\t\t|\t6")
        print("--------------------------------------------")
        print()

    def printExit(self):
        os.system("clear")
        print("Goodbye!")