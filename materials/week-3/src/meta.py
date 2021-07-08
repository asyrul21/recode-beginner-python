#############################
# Arrays and methods
#############################

# an array of members
members = ["Mike", "Bob", "Siti", "John"]

# return true if the name passed is present in the members list above
def isMember(name):
    return name in members

comedyBooks = [
    "Three Men In a Boat",
    "Born a Crime",
    "Let's Pretend This Never Happened"
]

scienceFictionBooks = [
    "Star Wars",
    "The Lord of the Rings",
    "Avatar"
]

thrillerBooks = [
    "The Girl on the Train",
    "The Silence of the Lamb",
    "The Da Vinci Code"
]

def isScienceFiction(book):
    return book in scienceFictionBooks

def isThriller(book):
    return book in thrillerBooks

def isComedy(book):
    return book in comedyBooks



members = ["Bob21", "John12", "Siti93", "Ali44"]
userName = input("Insert your username: ")

if(userName in members):
    print("Logged in successfully. Welcome back!")
else:
    print("Access denied. You are not a member.")