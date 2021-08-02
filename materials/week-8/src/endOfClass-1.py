# The first part of the End of Class exercise is to learn how
# to import external and local libraries.
# 1. From the folder helper, there's a file named JsonReadWriter.py
#   from that folder, import the class JsonReadWriter
# 2. Instantiate the JsonReadWriter class by passing in the path
#   to the data file. The data is in `data/json/students.json`
# 3. Load the Json data and store in a variable, using the JsonReadWriter's `load()`
#   method. Print the result if necessary.
# 4. Import the pprint library
# 5. Instantiate the pprint class by calling `pprint.PrettyPrinter(indent=4)`
# 6. Now, use the pprint instance you created to display the data nicely to screen, by
#   calling its `pprint(data)` instance method.
# 7. Display the third student's names, class, and mobile number to the screen nicely.


from helper.JsonReadWriter import JsonReadWriter
import pprint

jsonRW = JsonReadWriter("data/json/students.json")
data = jsonRW.load()

# print(data)
pp = pprint.PrettyPrinter()
pp.pprint(data)

thirdStudent = data[2]

# exercise to help understanding on how to access data
print()
print("Name: " + thirdStudent["firstName"] + " " + thirdStudent["lastName"])
print("Class: " + thirdStudent["class"])
print("Mobile: " + thirdStudent["contact"]["mobile"])








