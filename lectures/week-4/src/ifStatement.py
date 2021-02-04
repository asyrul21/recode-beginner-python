# import helper methods
from meta import isMember, isComedy, isScienceFiction, isThriller 

#############################
# Main
#############################

totalPrice = 0
if (isMember("John")):
	bookPrice = 12.00	
else:
	bookPrice = 20.0
totalPrice = totalPrice + bookPrice

print("Total price for John: " + str(totalPrice))
print("========================")

totalPrice = 0
if (isMember("Abu")):
	bookPrice = 12.00	
else:
	bookPrice = 20.0
totalPrice = totalPrice + bookPrice

print("Total price for Abu: " + str(totalPrice))
print("========================")

#############################
# Multi condition
#############################
bookPrice = 50
bookName = "Star Wars"
if (isScienceFiction(bookName)):
	discount = 10
elif (isThriller(bookName)):
	discount = 15
elif (isComedy(bookName)):
	discount = 5
else:
	discount = 20
totalPrice = bookPrice * (100 - discount) / 100
print("Multi Condition If Statement")
print("Book name: " + bookName)
print("Total price: " + str(totalPrice))
print("========================")

#############################
# Nested If
#############################
print("Nested If Statement")
print("========================")
number = 85
if (number >= 80):
	if(number <= 100):
		print("You scored an A!")
else:
	print("Nope, you did not get an A.")


