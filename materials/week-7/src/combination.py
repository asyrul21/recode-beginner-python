# creating a person class
class Person:
    # the constructor
    def __init__(self, firstName, lastName, age):
        # define instance variables (attributes) here
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    # define methods here
    def sayHello(self):
        print("Hi!")

    def introduceSelf(self):
        fullName = self.firstName + " " + self.lastName
        print("My name is " + fullName + ". I am " + str(self.age) + " years old!")


# creating 3 instances of the Person class
person1 = Person("Bob", "Marley", 27)
person2 = Person("Mike", "Tyson", 35)
person3 = Person("Siti", "Aminah", 30)


# putiing person instances into a list
print("Putting person instances into a list:")
# create a list of friends
friends = [ person1, person2, person3 ]

# referencing a friend item from list
friends[0].sayHello()
friends[0].introduceSelf()

# putiing person instances into a dictionary
print()
print("Putting person instances into a dictionary:")
# create a list of friends
friendsDict = {
    "bob" : person1,
    "mike": person2,
    "siti": person3
}

# referencing a friend item from list
friendsDict["mike"].sayHello()
friendsDict["mike"].introduceSelf()

