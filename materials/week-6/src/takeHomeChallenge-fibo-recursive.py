# This challenge has 2 parts. The first one is to write a function to produce the fibonacci sequence in a list
# or array. But you have to do it recursively, and NOT using a loop.
# This function takes a number as argument and a default argument of [0,1].
# 1. Ask from a user for a number. e.g. 5
# 2. This function will generate the fibonacci sequence containing no more than the number
# given by the user in step 1. If user gave 5, then there should be 5 numbers in the list
# 3. The second part of the challenge is to write a function to accept a list as parameter
# which the function will convert the list to a string of text, seperated by a comma
# This function uses a loop.

def fiboRecursion(number, sequence=[0, 1]):
    ...

def buildStringFromList(listArray):
    ...

number = input("How many numbers do you want in the Fibonacci sequence?: ")
number = int(number)

# call your methods here
fibonacciList = ...
output = ...

print(output)
