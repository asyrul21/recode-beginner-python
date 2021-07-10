from .Utility import clearScreen

class NavigationDisplay:
    def __init__(self):
        ...

    def printMainMenu(self):
        print("----------------------------------------------------")
        print("Activity\t\t\t\t| Selection")
        print("----------------------------------------------------")
        print("Create new Memorable Date\t\t|\t1")
        print("See what happened Today, years ago\t|\t2")
        print("Delete a Memorable Date\t\t\t|\t3")
        print("Search for Event by Name\t\t|\t4")
        print("Exit\t\t\t\t\t|\t5")
        print("----------------------------------------------------")
        print()

    def printExit(self):
        clearScreen()
        print("Goodbye!")