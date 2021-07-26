# function to return True of even, else False

def isEven(number):
    if(num % 2 == 0):
        return True
    else:
        return False

for num in range(0, 101):
    if(isEven(num)):
        print(num)
