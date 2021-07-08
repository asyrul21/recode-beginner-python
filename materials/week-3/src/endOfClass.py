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

# 1, 2 and 3 have been done for you...
score = input("Please insert your score: ")
grade = ""
message = ""
score = float(score)

if(score >= 80 and score <= 100):
    grade = "A"
    # if(score % 2 == 0):
    #     print("your score is an even number!")
elif(score >= 60 and score <= 79):
    grade = "B"

###########################

if(grade == "A"):
    message = "Congratulations, you scored an A!"
elif(grade == "E"):
    message = "Sorry, you failed the test."
else:
    message = "You score a " + grade

print(message)
