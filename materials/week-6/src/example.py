print("Week 6!")


def multipleBy1000(num):
    num = num * 1000
    return num

def addSomeone(arr, name):
    return arr.append(name)

number = 10
print("Number: " + str(number))

multipleBy1000(number)
print("Number: " + str(number))

myFriends = ["ali", "abu", "john"]
print("My friends: ")
print(myFriends)

addSomeone(myFriends, "Harry")
print(myFriends)
