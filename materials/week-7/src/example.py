
inputOK = False

while(inputOK == False):
    try:
        number = input("Please insert a number: ")
        number = float(number)
        if(number > 1000):
            raise Exception("Number cannot be more than 1000")
        inputOK = True
    except Exception as err:
        print("Invalid input!")
        print("ERROR:" + str(err))


print("your number: ", str(number))