# The formula is BMI = weight(kg) / height (m) ^ 2
# - Underweight: < 18.5
# - Normal: 18.5 - 24.9
# - Overweight: 25 - 29.9
# - Obese: > 30

def getFloatInput(message):
    floatInput = input(message)
    return float(floatInput)

def calculateBMI(height, weight):
    return weight / (height * height)

def getBMIResult(bmi):
    if(bmi < 18.5):
        return "Underweight"
    elif(bmi >= 18.5 and bmi <= 24.9):
        return "Normal"
    elif(bmi >= 25 and bmi <= 29.9):
        return "Overweight"
    else:
        return "Obese"

def outputResult(bmi, result):
    print("Your BMI is: " + str(bmi))
    print("You are " + result)


# main
userHeight = getFloatInput("Please insert your height in meters: ")
userWeight = getFloatInput("Please insert your weight in KG: ")
bmi = calculateBMI(userHeight, userWeight)
result = getBMIResult(bmi)
outputResult(bmi, result)





