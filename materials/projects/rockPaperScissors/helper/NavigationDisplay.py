import os

class NavigationDisplay:
    def __init__(self):
        ...

    def printMoves(self):
        print("--------------------------------------------")
        print("Move\t\t\t\t| Selection")
        print("--------------------------------------------")
        print("Rock\t\t\t\t|\t1")
        print("Paper\t\t\t\t|\t2")
        print("Scissors\t\t\t|\t3")
        print("--------------------------------------------")
        print()

    def displayHUD(self, player1score, player2score, round):
        os.system("clear")
        print("--------------------------------------------------")
        print("\t\t      Round: " + str(round))
        print("--------------------------------------------------")
        print()
        self.printMoves()
        print()
        print("--------------------------------------------------")
        print("\t\t      Score")
        print("--------------------------------------------------")
        print("Player 1: " + str(player1score) + "\t\tPlayer 2: " + str(player2score))
        print("==================================================")
        print()

    def printExit(self):
        os.system("clear")
        print("Goodbye!")