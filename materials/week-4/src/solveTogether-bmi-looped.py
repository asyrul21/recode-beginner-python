# looped BMI Calculator

print("******************************************")
print("*** WELCOME TO THE BODY MASS INDEX CALCULATOR ***")
print("******************************************")
print()

repeat = True
while(repeat == True):
    userHeight = input("Please insert your height in meters: ")
    userHeight = float(userHeight)

    userWeight = input("Please insert your weight in KG: ")
    userWeight = float(userWeight)

    bmi = userWeight / (userHeight * userHeight)

    result = ""
    if(bmi < 18.5):
        result = "Underweight"
    elif(bmi >= 18.5 and bmi <= 24.9):
        result = "Normal"
    elif(bmi >= 25 and bmi <= 29.9):
        result = "Overweight"
    else:
        result = "Obese"

    print("Your BMI is: " + str(bmi))
    print("You are " + result)
    print()

    ans = input("Calculate another one? (Y/N): ")
    if(ans == "N" or ans == "n"):
        repeat = False

print("Bye!")


