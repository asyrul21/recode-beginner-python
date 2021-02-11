print("A Function to Add 2 Numbers")
# Defining a function
def addTwoNumbers(num1, num2):
    result = num1 + num2
    return result

# Calling the function
total = addTwoNumbers(5, 2)
print("Total: " + str(total))
print("10 + 5 = " + str(addTwoNumbers(10, 5)))
print("21 + 4 = " + str(addTwoNumbers(21, 4)))
print("12 + 4 = " + str(addTwoNumbers(12, 4)))
print("18 + 2 = " + str(addTwoNumbers(18, 2)))

print()
print("Function to Calculate the volume of spheres")
def calculateVolumeOfSphereGivenRadius(radius):
    pi = 3.14159
    radiusCubic = radius * radius * radius
    volume = (4/3) * pi * radiusCubic
    return volume

radii = [10, 5, 6, 8, 9]

for radius in radii:
    volume = calculateVolumeOfSphereGivenRadius(radius)
    print("The volume of sphere with radius " + str(radius) + " is " + str(volume))