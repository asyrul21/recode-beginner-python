# Help user identify her grade based on her score
# 1. Use the input() syntax to get the exam score of the user
# 2. Store this input ina variable called `score`
# 3. Cast this score variable to a float
# 4. Use if statements to identify the grade of this score. Use the following rules:
#   - if score > 100 : tell user that the score is invalid
#   - if score is between 80 < x < 100 inclusive, then the frade is an A
#   - if score is between 60 < x < 79 inclusive, then the frade is an B
#   - if score is between 50 < x < 59 inclusive, then the frade is an C
#   - if score is between 40 < x < 49 inclusive, then the frade is an D
#   - if score < inclusive 39, then the grade is an E
#
# 5. Use another if statement, to output the user according to the following rules:
#   - if grade is A, then output "Congratulations! You scored an A!"
#   - if grade is E, then output "We are sorry to inform you that you have failed the test"
#   - for all other cases, output "You scored a [the grade]"

score = input("Please insert your score: ")
grade = ""

score = float(score)
if(score > 100 or score < 0):
    print("Your score is invalid!")
    exit()
elif(score >= 80 and score <= 100):
    grade = "A"
elif(score >= 60 and score <= 79):
    grade = "B"
elif(score >= 50 and score <= 59):
    grade = "C"
elif(score >= 40 and score <= 49):
    grade = "D"
elif(score <= 39):
    grade = "E"

if(grade == "A"):
    message = "Congratulations, you scored an A!"
elif(grade == "E"):
    message = "We are sorry to inform you that you have failed the test"
else:
    message = "You have scored a " + grade

print(message)

