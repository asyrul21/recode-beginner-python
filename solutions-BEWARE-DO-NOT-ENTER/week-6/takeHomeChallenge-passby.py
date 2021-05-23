# This is to demonstrate the concept of pass by reference

# when passing simple data types such as a number
# it is a pass by value
# the function does not alter the original data
# this is because such data types are immutable - cannot be changed

def multiplyBy2(num):
    # we are merely overwriting the num function argument
    num = num * 2

number = 21
multiplyBy2(number)

print("Number: " + str(number))

# however lists or arrays are mutable
# if you pass this list to a method, it will be a pass by reference

def addNewStudent(studentList, name):
    # notice we are not returning anything
    studentList.append(name)


myArray = ["Ali", "John", "Bob"]
addNewStudent(myArray, "Michael")

print("My Array:")
print(myArray)
# yet the original list is altered

# some references
# https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
# https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference