# The countdown program
import time

print("Welcome to the Countdown Program")

number = 10
while(number >= 0):
    print(number)

    time.sleep(1)

    number = number - 1

print("KABOOM")