# This challenge has 2 parts. The first one is to write a function to produce the fibonacci sequence in a list
# or array. But you have to do it recursively, and NOT using a loop.
# This function takes a number as argument and a default argument of [0,1].
# 1. Ask from a user for a number. e.g. 5
# 2. This function will generate the fibonacci sequence containing no more than the number
# given by the user in step 1. If user gave 5, then there should be 5 numbers in the list
# 3. The second part of the challenge is to write a function to accept a list as parameter
# which the function will convert the list to a string of text, seperated by a comma.
# This function uses a loop.

def fiboRecursion(number, sequence=[0, 1]):
    # base condition
    if(number <= 1):
        return [0]
    elif(number == 2):
        return sequence
    if(number - 2 == 0):
        return sequence

    sequence.append(
            sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    )
    return fiboRecursion(number - 1, sequence)

def buildStringFromList(listArray):
    output = ""
    for index, item in enumerate(listArray):
        if(index != len(listArray) - 1):
            output = output + str(item) + ", "
        else:
            output = output + str(item)
    return output

number = input("How many numbers do you want in the Fibonacci sequence?: ")
number = int(number)

fibonacciList = fiboRecursion(number)
output = buildStringFromList(fibonacciList)

print(output)
