# The formula is BMI = weight(kg) / height (m) ^ 2
# - Underweight: < 18.5
# - Normal: 18.5 - 24.9
# - Overweight: 25 - 29.9
# - Obese: > 30

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