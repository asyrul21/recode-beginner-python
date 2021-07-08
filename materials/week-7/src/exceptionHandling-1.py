print("Welcome to the Division Calculator")
print()

number1 = input("Insert the first number: ")
number1 = float(number1)

number2 = input("What would you like to divide that number with?: ")
number2 = float(number2)

try:
    result = number1 / number2
    print("Answer: " + str(result))
except Exception as err:
    print("Oops something went wrong. ERROR: " + str(err))
    print("Please make sure you are not performing division by 0")






