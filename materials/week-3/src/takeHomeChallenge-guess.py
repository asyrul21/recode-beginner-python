# The Number Guessing Game
# 1. Generate a random number between 1 - 10 inclusive
# 2. Declare a variable named `correct` and assign to it the value False
# 3. Asks the user to guess the number
# 4. MAKE SURE to cast the user input to integer
# 5. If the user gets it right, output "Congratulations! Your guess was correct!" and set the variable `correct` to True
# 6. otherwise, let the user know if the selected number is greater than or less than the actual number
# 7. This process will be looped while correct is False, until user gets it right. We will learn about loops next week!

# Step 1 and 2 have already been done for you
import random

print("******************************************")
print("*** WELCOME TO THE NUMBER GUESSING GAME ***")
print("******************************************")
print()
print("Guess the number between 1 and 10 inclusive!")
print()

randomNumber = random.randint(1, 10)
correct = False

while(correct == False):
    #     your logic goes here
    guess = input("Insert your guess: ")
    guess = int(guess)

    if(guess == randomNumber):
        correct = True
        print("Congratulations! Your guess was correct!")
    elif(guess > randomNumber):
        print("Your guess is more than the answer!")
    elif(guess < randomNumber):
        print("Your guess is less than the number")

print("Bye!")

