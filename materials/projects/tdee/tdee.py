# BMI Calculator
import os

#################### helper methods #######################
def calculateBMRforMale(height, weight, age):
    return (10 * weight) + (6.25 * height) - (5 * age) + 5

def calculateBMRforFemale(height, weight, age):
    return (10 * weight) + (6.25 * height) - (5 * age) - 161

def getPALValue(palID):
    if(palID == 1):
        return 1.2
    elif(palID == 2):
        return 1.375
    elif(palID == 3):
        return 1.55
    elif(palID == 4):
        return 1.725
    elif(palID == 5):
        return 1.9
    else:
        raise Exception("Invalid input passed to the get PAL method.")

###########################################################
# MAIN
###########################################################



repeat = True
while(repeat):
    os.system("clear")
    # if windows u use cls
    print("******************************************")
    print("***** WELCOME TO THE TDEE CALCULATOR *****")
    print("******************************************")
    print("ctrl + C to quit")
    print()
    height = input("Please insert your height in cm: ")
    height = float(height)

    weight = input("Please insert your weight in KG: ")
    weight = float(weight)

    age = input("Please insert your age as a whole number: ")
    age = int(age)

    gender = input("Are you male or a female? Type M for Male and F for female: ")

    BMR = 0
    if(gender == "M" or gender == "m"):
        BMR = calculateBMRforMale(height, weight, age)
    else:
        BMR = calculateBMRforFemale(height, weight, age)

    print()
    print("========================================================================")
    print("ID\t||\tLifestyle")
    print("------------------------------------------------------------------------")
    print("1\t||\tSedentary (little or no exercise + work a desk job)")
    print("------------------------------------------------------------------------")
    print("2\t||\tLightly Active (light exercise 1-3 days per week)")
    print("------------------------------------------------------------------------")
    print("3\t||\tModerately Active (moderate exercise 3-5 days per week)")
    print("------------------------------------------------------------------------")
    print("4\t||\tVery Active (heavy exercise 6-7 days per week)")
    print("------------------------------------------------------------------------")
    print("5\t||\tExtremely Active (very heavy exercise, hard labor job)")
    print("========================================================================")
    print()

    palID = input("Based on the table above, insert the ID (1-5) which describes your lifestyle the closest: ")
    palID = int(palID)

    pal = getPALValue(palID)
    TDEE = BMR * pal

    print()
    print("Your Total Daily Energy Requirement is: " + str(TDEE) + "kCal")
    print()
    ans = input("Calculate another? (Y/N): ")

    repeat = False if ans == "N" or ans == "n" else True

os.system("clear")
# if windows u use cls
print("Goodbye!")


