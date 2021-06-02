import time

print("**********************************")
print("Welcome to the countdown program!")
print("**********************************")
print() # print empty line

# a loop from 10 to 0, increment by -1 / decrease by 1
for i in range(10, 0, -1):

    # print to screen the number
    print(i)

    # sleep for 1 second
    time.sleep(1)

print()
print("KABOOM!")
print("CONGRATULATIONS!")
print("YOU HAVE EXECUTED YOUR FIRST PYTHON PROGRAM!")
