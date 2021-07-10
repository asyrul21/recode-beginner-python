# The Fibonacci Sequence Generator

fiboSequence = []

for index, number in enumerate(range(0, 1000)):
    if(index == 0 or index == 1):
        fiboSequence.append(number)
    else:
        nextNumber = fiboSequence[index - 1] + fiboSequence[index - 2]
        fiboSequence.append(nextNumber)

        if(nextNumber > 1000):
            break


result = fiboSequence[:-1]
output = ""

for index, item in enumerate(result):
    if(index != len(result) - 1):
        output = output + str(item) + ", "
    else:
        output = output + str(item)

print(output)

    



