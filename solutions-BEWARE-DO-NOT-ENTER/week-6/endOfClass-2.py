# The second part of the end of class exercise is to write a function which concatenates
# string variables.
# We first ask the user for his first name.
# Then we ask the user for his last name.
# These two variables will be passed into a function which will concatenate these names.
# Finally, we output to screen the full name

def getFullName(fname, lname):
    return fname + " " + lname

firstName = input("Your first name: ")
lastName = input("Your last name: ")

output = getFullName(firstName, lastName)
print("Your full name is: " + output)