###############################################################
# do not modify the code in here ##############################
from helper.TxtReader import TxtReader
import os

DATA_PATH = "text.txt"

# load data
txtReader = TxtReader(DATA_PATH)
rawSentence = txtReader.load()

# do not delete the code in here ##############################
###############################################################
# 1. find a way to split a stirng variable into a list of words. We split them by a space
# eg. "I love pepperoni pizzas" -> ["I", "love", "peperoni", "pizzas"]
# HINT: use google to help you
# 2. Initialise an empty dictionary and give it the name `wordsSummary`
# 3. Write a loop through the list of words you made in (1). If the dictionary key does not exists, create new key
# and assign the value of 1 to it
# 4. Otherwise, update the value of this key by adding itself by 1
# 5. Write a function to print a dictionary nicely.
# 6. Call this function at the end of your program


def printDictionary(wordDictionary):
    ...

## word counting logic goes here