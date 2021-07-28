def isEven(num):
    return num % 2 == 0

numbers = range(1, 20)

for number in numbers:
    if(isEven(number)):
        print(str(number) + " is even")