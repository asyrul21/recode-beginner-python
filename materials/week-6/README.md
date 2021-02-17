# Lesson 6: Functions and Recursions

## Functions

From `src/functions.py`

```python
print("A Function to Add 2 Numbers")
# Defining a function
def addTwoNumbers(num1, num2):
    result = num1 + num2
    return result

# Calling the function
total = addTwoNumbers(5, 2)
print("Total: " + str(total))
print("10 + 5 = " + str(addTwoNumbers(10, 5)))
print("21 + 4 = " + str(addTwoNumbers(21, 4)))
print("12 + 4 = " + str(addTwoNumbers(12, 4)))
print("18 + 2 = " + str(addTwoNumbers(18, 2)))

print()
print("Function to Calculate the volume of spheres")
def calculateVolumeOfSphereGivenRadius(radius):
    pi = 3.14159
    radiusCubic = radius * radius * radius
    volume = (4/3) * pi * radiusCubic
    return volume

radii = [10, 5, 6, 8, 9]

for radius in radii:
    volume = calculateVolumeOfSphereGivenRadius(radius)
    print("The volume of sphere with radius " + str(radius) + " is " + str(volume))
```

Output:

```bash
A Function to Add 2 Numbers
Total: 7
10 + 5 = 15
21 + 4 = 25
12 + 4 = 16
18 + 2 = 20

Function to Calculate the volume of spheres
The volume of sphere with radius 10 is 4188.786666666666
The volume of sphere with radius 5 is 523.5983333333332
The volume of sphere with radius 6 is 904.7779199999999
The volume of sphere with radius 8 is 2144.658773333333
The volume of sphere with radius 9 is 3053.6254799999997
```

## Recursions

Factorial Example, from `src/recursion.py`

```python
def factorial(number):
    # set a base condition
    if(number == 0 or number == 1):
        return 1

    # call itself
    return number * factorial(number - 1)


# calling the function
print("Factorial of 5 is: " + str(factorial(5)))
print("Factorial of 7 is: " + str(factorial(7)))
```

Output:

```bash
This is a recursive function to calculate the factorial value of a number.
Factorial of 5 is: 120
Factorial of 7 is: 5040
```

# End of Class Exercise

There are two files which you need to solve:

- `src/endOfClass-1.py`
- `src/endOfClass-2.py`

## The First Part

1. Follow the instructions in `src/endOfClass-1.py`

2. Run your code by typing

   ```python
   python endOfClass-1.py
   ```

3. Your output should look something like this:

   ```bash
   Printing odd numbers
   1 is an odd number
   3 is an odd number
   5 is an odd number
   7 is an odd number
   9 is an odd number
   11 is an odd number
   13 is an odd number
   15 is an odd number
   17 is an odd number
   19 is an odd number
   ```

## The Second Part

1.  Follow the instructions in `src/endOfClass-2.py`

2.  Run your code by typing

    ```python
    python endOfClass-2.py
    ```

3.  Your output should look something like this:

    ```bash
    Your first name: John
    Your last name: Wick
    Your full name is: John Wick
    ```

    ```bash
    Your first name: Bob
    Your last name: the Builder
    Your full name is: Bob the Builder
    ```

    <br/>

# Take Home Challenge

## Part 1: The Hard Part

This is a faily chellenging task. The following concepts may help you:

- Optional Arguments. When defining functions, you can add an optional argument, by giving it a _default value_. For example:

  ```python
  def multiplyTwoNumbers(num1, num2=1):
      return num1 * num2
  ```

  In the code above, the `num2` argument is optional, and has a default value of 1. That way, callers of the function can omit the second argument, because it already has a default value. Example call:

  ```python
  product = multiplyTwoNumbers(5) # this returns 5
  product2 = multiplyTwoNumbers(5, 6) # this returns 30
  ```

- List methods, such as `append` and accessing specific elements using indices.

- inputs and casting

- If statements

- the for enumerate loop

<br/>

### Execution

1. Follow the instructions in `src/takeHomeChallenge-fibo-recursive.py`

2. Run your code by typing

   ```python
   python takeHomeChallenge-fibo-recursive.py
   ```

3. Your output should look something like this:

   ```bash
   How many numbers do you want in the Fibonacci sequence?: 5
   0, 1, 1, 2, 3
   ```

   ```bash
   How many numbers do you want in the Fibonacci sequence?: 10
   0, 1, 1, 2, 3, 5, 8, 13, 21, 34
   ```

## Part 2: The Easy Part

Read on articles on the web about:

_Passing by Value vs Passing by Reference_

This is a crucial concept in programming. Althought in Python variables are passed into functions by reference. However, in other languages like C++, you may choose either to pass by reference or value. Therefore, it is essential for you to know the difference between the two.

An example of such article can be found [here](https://www.educative.io/edpresso/pass-by-value-vs-pass-by-reference).
