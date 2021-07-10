# output even numbers only
# it is crucial to note that range() returns an array/list

print("Even Numbers:")
for number in range(1, 50):
    if number % 2 == 0:
        print(number)