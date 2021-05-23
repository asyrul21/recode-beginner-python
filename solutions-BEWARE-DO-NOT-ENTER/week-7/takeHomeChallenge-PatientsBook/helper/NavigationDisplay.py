from .Utility import clearScreen

class NavigationDisplay:
    def __init__(self):
        ...

    def printMainMenu(self):
        print("--------------------------------------------")
        print("Activity\t\t\t| Selection")
        print("--------------------------------------------")
        print("Create new contact\t\t|\t1")
        print("Search for Contact by Name\t|\t2")
        print("Edit Record\t\t\t|\t3")
        print("Exit\t\t\t\t|\t4")
        print("--------------------------------------------")
        print()

    def printExit(self):
        clearScreen()
        print("Goodbye!")