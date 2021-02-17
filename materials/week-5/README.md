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

### Some Pre Requisites

In order to solve this problem, you need to take note on a few things:

- You may need to use the `range()` method, as explained from your endOfClass exercise. The `range()` method returns an _array_ (or sometimes refered to as _list_).

- You may then wrap your `range()` with `enumerate()` to get access to the index of each number.

- Another thing you need to know is the `break` statement. The `break` statement deliberately _STOPS_ a loop and get out of it: hence the sub title in the first slide. Example usage:

  ```python
  for i in range(0, 10):
      print(i)
      if i == 5:
          break
  ```

- The code above outputs numbers from 0 to 5, but exit the loop right after that.

- Another important thing is `Array Slicing`. All arrays and strings can be sliced. Slicing means to only take portion of the collection. Example usage:

  ```python
  myArray = ["Ali", "Mike", "John", "Siti", "Robert"]

  sliced = myArray[0:3]

  print(sliced)
  ```

- The code above sliced the array from location 0 to 3. Output:

  ```bash
  ['Ali', 'Mike', 'John']
  ```

- You also need to know the `append()` method. Every array can call this method simply to _ADD ITEMS_ to itself. Example:

  ```python
  myArray = ["Ali", "Mike", "John", "Siti", "Robert"]

  myArray.append("Harry")

  print(myArray)
  ```

- Output:

  ```bash
  ['Ali', 'Mike', 'John', 'Siti', 'Robert', 'Harry']
  ```

- Finally, you need to know the `len()` method, which simply returns the size of an array. Example usage:

  ```python
  myArray = ["Ali", "Mike", "John", "Siti", "Robert"]
  print(len(myArray))
  ```

- The code above prints 5, because there are 5 elements in the array.

- The `len()` method is useful to get the last item in the array. Example:

  ```python
  myArray = ["Ali", "Mike", "John", "Siti", "Robert"]

  lastItem = myArray[len(myArray) - 1]
  print(lastItem)
  ```

- The code above returns "Robert" because that's the last item. Note that we minus 1 because array indices start at 0.

### Execution

1. Follow the instructions in `src/takeHomeChallenge-fibo.py`

2. Run your code by typing

   ```python
   python takeHomeChallenge-fibo.py
   ```

3. Your output should look something like this:

   ```bash
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
   ```

4. Please note that we do NOT want to output a list. Use a loop to concatenate an initialised string, so we can get an output similar to the one above.

   <br/>

## Palindrome Checker

A Palindrome is a word which when spelled backwards, becomes the same word. [Palindromes](https://examples.yourdictionary.com/palindrome-examples.html)

For example: Noon, Racecar, Rotator, Level, etc..

### Some Pre Requisites

To Solve this problem, you may need to know a few things:

- All that you need to know to solve the Fibonacci problem above

- You need to know the `lower()` statement, which is accessible from all string variables. It simple converts the string to all lower case. This helps when you want to make your interface case insensitive whenever the user keys in Example usage:

  ```python
  name = "John Connor"

  print(name.lower())
  ```

- output:

  ```bash
  john connor
  ```

### Execution

1. Follow the instructions in `src/takeHomeChallenge-palindrome.py`

2. Run your code by typing

   ```python
   python takeHomeChallenge-palindrome.py
   ```

3. Your output should look something like this:

   ```bash
   Welcome to the Palindrome Checker

   Insert a word: racecar

   This is a palindrome!
   ```

   ```bash
   Welcome to the Palindrome Checker

   Insert a word: Alphabet

   Nope this is not.
   ```
