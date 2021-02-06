# All About Loops

## The While Loop

From `src/while.py`

```python
number = 1
while(number < 11):
    print(str(number))
    number = number + 1
```

## The For Loop

From `src/for.py`

```python
students = [ "Ali", "Abu", "John", "Siti", "Bob" ]

print("The For In Loop")
print("Print Students who name starts with an A:")
for student in students:
    if student[0] == "A" or student[0] == "a":
        print(student)

print()
print("The For in Enumerate Loop")
for index, student in enumerate(students):
    print("Index: " + str(index) + " Name: " + student)

print()
print("Print Only Student at 2nd and 3rd Position:")
for index, student in enumerate(students):
    if(index == 1 or index == 2):
        print(student)
```

<br/>

# End of Class Exercise

1. Follow the instructions in `src/endOfClass.py`

2. Run your code by typing

   ```python
   python endOfClass.py
   ```

3. Your output should look something like this:

   ```bash
   The Multiples of 3:
    3
    6
    9
    12
    15
    18

    Odd Numbers:
    1
    3
    5
    7
    9
    11
    13
    15
    17
    19
   ```

   <br/>

# Take Home Challenge

There are two parts to this challenge:

1. Output a Fibonacci Sequence between 0-1000
2. Palindrome Checker

## Fibonacci Sequence

A Fibonacci sequence is a sequence of which the following number is the sum of the previous 2 numbers, starting from 0. [The Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number)

`Example: 0, 1, 1, 2, 3, 5, 8, ...`

3 is the sum of 1 and 2, 5 is the sum of 2 and 3, and so on.

HINT: You may need to use the `range()` method, as explained from your endOfClass exercise.

1. Follow the instructions in `src/takeHomeChallenge-fibo.py`

2. Run your code by typing

   ```python
   python takeHomeChallenge-fibo.py
   ```

3. Your output should look something like this:

   ```bash

   ```

   <br/>

## Palindrome Checker

A Palindrome is a word which when spelled backwards, becomes the same word. [Palindromes](https://examples.yourdictionary.com/palindrome-examples.html)

For example: Noon, Racecar, Rotator, Level, etc..

1. Follow the instructions in `src/takeHomeChallenge-palindrome.py`

2. Run your code by typing

   ```python
   python takeHomeChallenge-palindrome.py
   ```

3. Your output should look something like this:

   ```bash

   ```
