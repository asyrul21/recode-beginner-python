# Lesson 4: Conditional Statements, If Statements and Inputs

## If Statements

From `src/ifStatement.py`

```python
# import helper methods
from meta import isMember, isComedy, isScienceFiction, isThriller

#############################
# Main
#############################

totalPrice = 0
if (isMember("John")):
	bookPrice = 12.00
else:
	bookPrice = 20.0
totalPrice = totalPrice + bookPrice

print("Total price for John: " + str(totalPrice))
print("========================")

totalPrice = 0
if (isMember("Abu")):
	bookPrice = 12.00
else:
	bookPrice = 20.0
totalPrice = totalPrice + bookPrice

print("Total price for Abu: " + str(totalPrice))
print("========================")


#############################
# Multi condition
#############################
bookPrice = 50
bookName = "Star Wars"
if (isScienceFiction(bookName)):
	discount = 10
elif (isThriller(bookName)):
	discount = 15
elif (isComedy(bookName)):
	discount = 5
else:
	discount = 20
totalPrice = bookPrice * (100 - discount) / 100
print("Multi Condition If Statement")
print("Book name: " + bookName)
print("Total price: " + str(totalPrice))


#############################
# Nested If
#############################
print("Nested If Statement")
print("========================")
number = 85
if (number >= 80):
	if(number <= 100):
		print("You scored an A!")
else:
	print("Nope, you did not get an A.")
```

<br/>

## Input

```python
print("**********************")
print("CM to M Converter")
print("**********************")
print()

userHeight = input("Enter your height in cm: ")
print("Converting to meter...")
heightInMeter = float(userHeight) / 100
print("Your height in meter is " + str(heightInMeter) + "m")
```

<br/>

# Solve Together References

## (Body Mass Index) BMI Calculator

The formula is BMI = weight(kg) / height (m) ^ 2

Categories:

    - Underweight: < 18.5
    - Normal: 18.5 - 24.9
    - Overweight: 25 - 29.9
    - Obese: > 30

[Reference 1](<https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator>)

[Reference 2](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm)

## TDEE (Total Daily Energy Expenditure) Calculator

Based on the [Harris-Benedict Equation](https://en.wikipedia.org/wiki/Harris–Benedict_equation):

TDEE = BMR \* Physical Activity Level (PAL)

BMR formula for men:

`BMR = 66.5 + ( 13.75 × weight in kg ) + ( 5.003 × height in cm ) – ( 6.755 × age in years )`

BMR for women:

`BMR = 655 + ( 9.563 × weight in kg ) + ( 1.850 × height in cm ) – ( 4.676 × age in years )`

PAL:

    - Sedentary (little to no exercise + work a desk job) = 1.2

    - Lightly Active (light exercise 1-3 days / week) = 1.375

    - Moderately Active (moderate exercise 3-5 days / week) = 1.55

    - Very Active (heavy exercise 6-7 days / week) = 1.725

    - Extremely Active (very heavy exercise, hard labor job, training 2x / day) = 1.9

[Reference 1](https://en.wikipedia.org/wiki/Harris–Benedict_equation)

[Reference 2](https://steelfitusa.com/2018/10/calculate-tdee/)

# End of Class Exercise

1. Follow the instructions in `src/endOfClass.py`

2. Run your code by typing

   ```python
   python endOfClass.py
   ```

3. Your output should look something like this:

   ```bash
   Please insert your score: 30
   We are sorry to inform you that you have failed the test
   ```

   ```bash
   Please insert your score: 1000
   Your score is invalid!
   ```

   ```bash
   Please insert your score: 95
   Congratulations, you scored an A!
   ```

   ```bash
   Please insert your score: 55
   You have scored a C
   ```

   <br/>

# Take Home Challenge

There are two parts to this challenge:

1. Number guessing game
2. Calculate Area of Rectangle, Triangle or Circle

## Number Guessing Game

This is a slightly challenging task, as it involves a loop. HINT: use the `while` loop.

1. Follow the instructions in `src/takeHomeChallenge-guess.py`

2. Run your code by typing

   ```python
   python takeHomeChallenge-guess.py
   ```

3. Your output should look something like this:

   ```bash
   ******************************************
   *** WELCOME TO THE NUMBER GUESSING GAME ***
   ******************************************

   Guess the number between 1 and 10 inclusive!

   Please insert your guess: 1
   Oops your guess is less than the answer!
   Please insert your guess: 5
   Oops your guess is more than the answer!
   Please insert your guess: 3
   Oops your guess is less than the answer!
   Please insert your guess: 2
   Oops your guess is less than the answer!
   Please insert your guess: 4
   Congratulations! Your guess was correct!
   ```

   <br/>

## Calculate Area of Rectangle, Triangle or Circle

1. Follow the instructions in `src/takeHomeChallenge-area.py`

2. Run your code by typing

   ```python
   python takeHomeChallenge-area.py
   ```

3. Your output should look something like this:

   ```bash
   ******************************************
   *** WELCOME TO THE SHAPE AREA CALCULATOR ***
   ******************************************


   Choose your shape. For rectangle, type R. For Triangle, type T, for circle, type C: x
   Invalid input!
   ```

   ```bash
   ******************************************
   *** WELCOME TO THE SHAPE AREA CALCULATOR ***
   ******************************************


   Choose your shape. For rectangle, type R. For Triangle, type T, for circle, type C: R
   Insert the height in m: 5
   Inser the width in m: 6
   The Area of the Rectangle is 30.0 meter squared.
   ```

   ```bash
   ******************************************
   *** WELCOME TO THE SHAPE AREA CALCULATOR ***
   ******************************************


   Choose your shape. For rectangle, type R. For Triangle, type T, for circle, type C: T
   Insert the height in m: 3
   Inser the width in m: 7
   The Area of the Triangle is 10.5 meter squared.
   ```

   ```bash
   ******************************************
   *** WELCOME TO THE SHAPE AREA CALCULATOR ***
   ******************************************


   Choose your shape. For rectangle, type R. For Triangle, type T, for circle, type C: C
   Insert the radius in m: 5
   The Area of the Circle is 78.53975 meter squared.
   ```
