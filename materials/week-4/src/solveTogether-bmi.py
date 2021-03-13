# The formula is BMI = weight(kg) / height (m) ^ 2
# - Underweight: < 18.5
# - Normal: 18.5 - 24.9
# - Overweight: 25 - 29.9
# - Obese: > 30

userWeight = input("Insert your weight in KG: ")
userWeight = float(userWeight)

userHeight = input("Insert your height in meters: ")
userHeight = float(userHeight)

bmiValue = userWeight / (userHeight * userHeight)
status = ""

if(bmiValue < 18.5):
    status = "underweight"
elif(bmiValue >= 18.5 and bmiValue <= 24.9):
    status = "normal"
elif(bmiValue >= 25 and bmiValue <= 29.9):
    status = "overweight"
else:
    status = "obese"


print("Your BMI is: " + str(bmiValue))
print("You are " + status)