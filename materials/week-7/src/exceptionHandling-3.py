print("Exception Handling Example Problem 3: Reading/Writing to Files")

import json
import pprint # https://docs.python.org/3/library/pprint.html
pp = pprint.PrettyPrinter(indent=4)

try:
    with open("data/studentsx.json", "r") as read_file:
        data = json.load(read_file)

    print("Read file success!")
    print("*********************")
    pp.pprint(data)
    print()
except IOError as ioerr:
    print("Failed to read file.")
    print("ERROR: " + str(ioerr))
except Exception as err:
    print("Oops something caused the program to crash and terminate")
    print("ERROR: " + str(err))

    