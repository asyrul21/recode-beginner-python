# function to return True of even, else False

def numberIsEven(num):
    return num % 2 == 0

result = numberIsEven(5)
print(result)

for num in range(0,100):
    print("NUM: " + str(num))
    print("Even: " + str(numberIsEven(num)))
    print()