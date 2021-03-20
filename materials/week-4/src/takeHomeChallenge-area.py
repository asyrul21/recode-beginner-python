# The Calculate Area of either Rectangle or Triangle
# 1. Ask user whether to calculate area of Rectangle or Triangle. To proceed with Rectangle, user needs to
#   input "r". To proceed with Triangle, user needs to input "t". etc. Note that these are case sensitive
#   For any other input, tell the user that the input is invalid.
# 2. Based on user choice, ask more information to allow you to perform the calculation.
#   For example, to calculate area of rectangle, you need to ask for width and length.
#   To calculate area of circle, you need ask for the radius.
# 3. Do not forget to cast the user input to float before performing calculation
# 4. Perform the calculation accordingly and output to the user.

print("******************************************")
print("*** WELCOME TO THE SHAPE AREA CALCULATOR ***")
print("******************************************")
print()
print()

shape = input("Choose your shape. For rectangle, type R. For Triangle, type T, for circle, type C: ")

shapeName = ""
area = 0.0

if(shape == "R"):
    shapeName = "Rectangle"
    height = input("Insert the height in m: ")
    height = float(height)

    width = input("Inser the width in m: ")
    width = float(width)

    area = height * width

elif(shape == "T"):
    shapeName = "Triangle"
    height = input("Insert the height in m: ")
    height = float(height)

    width = input("Inser the width in m: ")
    width = float(width)

    area = (height * width) / 2

elif(shape == "C"):
    shapeName = "Circle"
    radius = input("Insert the radius in m: ")
    radius = float(radius)
    pi = 3.14159

    area = pi * radius * radius

else:
    print("Invalid input!")
    exit()


print("The Area of the " + shapeName + " is " + str(area) + " meter squared.")



# how we want to output it:
# print("The Area of the " + shapeName + " is " + str(area) + " meter squared.")


