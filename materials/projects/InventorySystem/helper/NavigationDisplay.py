import os

class NavigationDisplay:
    def __init__(self):
        ...

    def printMainMenu(self):
        os.system("clear")
        print("--------------------------------------------")
        print("\t    The Inventory System")
        print("--------------------------------------------")
        print("Activity\t\t|\tSelection")
        print("--------------------------------------------")
        print("Show Inventory List\t|\t1")
        print("Add Item\t\t|\t2")
        print("Edit Item\t\t|\t3")
        print("Delete Item\t\t|\t4")
        print("Search Item By Name\t|\t5")
        print("Search Item By Category\t|\t6")
        print("Exit\t\t\t|\t7")
        print("--------------------------------------------")
        print()

    def printExit(self):
        os.system("clear")
        print("Goodbye!")