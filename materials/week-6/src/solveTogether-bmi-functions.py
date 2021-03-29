# BMI Calculator

def getFloatInput(message):
    userInput = input(message)
    return float(userInput)

def calculateBMI(weight, height):
    return weight / (height * height)

def getBMIStatus(bmiValue):
    if(bmiValue < 18.5):
        result = "Underweight"
    elif(bmiValue >= 18.5 and bmiValue <= 24.9):
        result = "Normal and Healthy"
    elif(bmiValue >= 25 and bmiValue <= 29.9):
        result = "Overweight"
    else:
        result = "Obese"
    return result

def displayToUser(bmiValue, status):
    print("Your body mass index is: " + str(bmiValue))
    print("You are " + status + ".")

print("******************************************")
print("*** WELCOME TO THE BODY MASS INDEX CALCULATOR ***")
print("******************************************")
print()

height = getFloatInput("Please insert your height in meters: ")
weight = getFloatInput("Please insert your weight in KG: ")
bmi = calculateBMI(weight, height)
result = getBMIStatus(bmi)
displayToUser(bmi, result)


