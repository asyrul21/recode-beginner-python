# BMI Calculator

def printBanner():
    print("******************************************")
    print("*** WELCOME TO THE BODY MASS INDEX CALCULATOR ***")
    print("******************************************")
    print()

def getFloatInput(text):
    item = input(text)
    return float(item)

def calculateBMI(weight, height):
    return weight / (height * height)

def getResultBasedOnBMI(bmi):
    if(bmi < 18.5):
        result = "Underweight"
    elif(bmi >= 18.5 and bmi <= 24.9):
        result = "Normal and Healthy"
    elif(bmi >= 25 and bmi <= 29.9):
        result = "Overweight"
    else:
        result = "Obese"

    return result

printBanner()

height = getFloatInput("Please insert your height in meters: ")
weight = getFloatInput("Please insert your weight in KG: ")
bmi = calculateBMI(weight, height)
result = getResultBasedOnBMI(bmi)

print("Your body mass index is: " + str(bmi))
print("You are " + result + ".")