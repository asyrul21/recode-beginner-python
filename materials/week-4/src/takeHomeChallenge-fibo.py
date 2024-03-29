# The Fibonacci Sequence Generator
# 1. declare and empty array of name fiboSequence
# 2. Use for loop with enumeration with a range method, between 0 - 1000
# 3. If number is 0 or 1, simple append it to the list
# 4. Otherwise, calculate the next number by adding the 2 numbers before it. Use array indices to do this.
# 5. Append this new number to the sequence.
# 6. Create a condition that, if this new number is more than 1000, break from the loop
# 7. Now, slice your fiboSequence to get all items except the last one, since that number is more that 1000
# 8. Initialise a string variable named output and assign the value "" to it.
# 9. using the for enumerate loop once again, concatenate the numbers in your sliced Array to from one long string
# 10. You should check that if it's not the last item, add comma (,) otherwise, don't add comma.

print("Welcome to the Fibonacci Sequence Generator!")

fiboSequence = []

# your loop here to create the sequence
for idx, number in  enumerate(range(0,1000)):
    if(idx == 0 or idx == 1):
        fiboSequence.append(number)
    else:
        nextNumber = fiboSequence[idx - 1] + fiboSequence[idx - 2]
        if(nextNumber > 1000):
            break
        fiboSequence.append(nextNumber)
        
output = ""

# another loop here to create output string
for index, item in enumerate(fiboSequence):
    if(index == len(fiboSequence) - 1):
        output = output + str(item)
    else:
        output = output + str(item) + ", "

print(output)

    



