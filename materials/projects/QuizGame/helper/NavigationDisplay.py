from .Utility import clearScreen

class NavigationDisplay:
    def __init__(self):
        ...

    def printMainMenu(self):
        print("--------------------------------------------")
        print("Activity\t\t\t| Selection")
        print("--------------------------------------------")
        print("Play\t\t\t\t|\t1")
        print("Show ScoreBoard\t\t\t|\t2")
        print("Exit\t\t\t\t|\t3")
        print("--------------------------------------------")
        print()

    def displayQuestionAndScore(self, question, score, answer=False):
        clearScreen()
        print("-------------------------------------------------------")
        print("\t\t\tScore: " + str(score))
        print("-------------------------------------------------------")
        print()
        print("\t" + question)
        print()
        if(answer):
            print("\tAnswer: " + str(answer))
        print()



    def printExit(self):
        clearScreen()
        print("Goodbye!")