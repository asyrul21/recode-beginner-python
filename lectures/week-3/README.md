# Week 3: Data Types, Referencing, Casting, Arithmetic

## Declaring and Referencing Variables

You may find this code snippet in `src/variables.py`

```python
# declaring string variable
myStringVariable = "Hello!"

# declaring number variable
myNumberVariable = 123

# declaring boolean variable
myBooleanVariable = True

# declaring an array of string
myArray = ["Ali", "Abu", "John", "Siti", "Bob"]

myMixedArray = [1 , 321.51, "John", True, "What is going on here??"]

# output those variable by referencing their name
print(myStringVariable)
print(myNumberVariable)
print(myBooleanVariable)
print(myArray)
print(myMixedArray)
```

## Arithmetic

You may find this code snippet in `src/arithmetic.py`

```python
# assign number variables
number1 = 100
number2 = 5

# assign string variables
string1 = "I love pizzas, "
string2 = "but sandwiches are better."

# adding
result = number1 + number2
print(result)

# concatenating
result = string1 + string2
print(result)

# minus numbers
result = number1 - number2
print(result)

# minus string
# will throw error
# result = string1 - string2
# print(result)

# multiply
result = number1 * number2
print(result)

# divide
result = number1 / number2
print(result)

# remainder
result = 9 % 2
print(result)

```

## Casting

You may find this code snippet in `src/casting.py`

```python
#****************************
# converting string to integer
#****************************
# declare a stirng variable
myVariable = "123"

# convert this string to integer number
myNumber = int(myVariable)

# your variable can now be added accordingly
result = myNumber + 1

# output to screen
print(result)

#****************************
# converting integer to string
#****************************
# declare an integer variable
myIntegerVariable = 45

# convert this integer to string
myStringVariable = str(myIntegerVariable)

# your variable can now be added accordingly
result = "I am " + myStringVariable + " years old."

# output to screen
print(result)

#****************************
# converting string to float
#****************************
# declare an string variable
myString = "3.1415926"

# convert this string to float number
myFloat = float(myString)

# your variable can now be added accordingly
result = myFloat * 80

# output to screen
print(result)
```
