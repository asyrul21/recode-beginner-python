print("Exception Handling Example Problem 2: Invalid Input")
print()

try:
    number1 = input("Insert a NUMBER: ")
    number1 = float(number1)
    print("Success!")
except ValueError as valueErr:
    print("Oops something went wrong. Please input NUMBERS ONLY!")
    print("ERROR: " + str(valueErr))
except Exception as err:
    print("Oops the system failed.")
    print("ERROR: " + str(err))

