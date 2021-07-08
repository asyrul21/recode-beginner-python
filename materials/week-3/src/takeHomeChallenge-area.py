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



# how we want to output it:
# print("The Area of the " + shapeName + " is " + str(area) + " meter squared.")
shape = input("Choose your shape. For rectangle, type R. For Triangle, type T, for circle, type C: ")

if(shape == "R" or shape == "r"):
    print("Calculate area of rectangle!")
    height = input("Insert height: ")
    height = float(height)

    width = input("Insert width: ")
    width = float(width)

    area = height * width
    print("The area of the rectangle is: " + str(area))

elif(shape == "T" or shape == "t"):
    print("Calculate area of triangle")
    height = input("Insert height: ")
    height = float(height)

    width = input("Insert width: ")
    width = float(width)

    area = (height * width) / 2
    print("The area of the triangle is: " + str(area))

elif(shape == "C" or shape == "c"):
    print("Calculation area of circle")
    pi = 3.14159

    radius = input("Insert the radius: ")
    radius = float(radius)
    area = pi * radius * radius

    print("The area of the circle is: " + str(area))

else:
    print("Invalid input!")
    exit()


