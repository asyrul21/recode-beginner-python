print("This is a recursive function to calculate the factorial value of a number.")

# define function
def factorial(number):
    # set a base condition
    if(number == 0 or number == 1):
        return 1

    # call itself
    return number * factorial(number - 1)


# calling the function
print("Factorial of 5 is: " + str(factorial(5)))
print("Factorial of 7 is: " + str(factorial(7)))