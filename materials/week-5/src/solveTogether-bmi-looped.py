# looped BMI Calculator

print("******************************************")
print("*** WELCOME TO THE BODY MASS INDEX CALCULATOR ***")
print("******************************************")
print()

repeat = True
while(repeat):
    height = input("Please insert your height in meters: ")
    height = float(height)

    weight = input("Please insert your weight in KG: ")
    weight = float(weight)

    bmi = weight / (height * height)

    result = ""
    if(bmi < 18.5):
        result = "Underweight"
    elif(bmi >= 18.5 and bmi <= 24.9):
        result = "Normal and Healthy"
    elif(bmi >= 25 and bmi <= 29.9):
        result = "Overweight"
    else:
        result = "Obese"

    print("Your body mass index is: " + str(bmi))
    print("You are " + result + ".")

    answer = input("Would you like to calculate a new one? (Y/N): ")

    if(answer == "N" or answer == "n"):
        repeat = False

    # repeat = False if answer == "N" or answer == "n" else True

print("Goodbye")
    

