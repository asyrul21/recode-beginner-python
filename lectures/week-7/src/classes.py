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

# each person calls their own introduceSelf() method/behaviour
person1.introduceSelf()
person2.introduceSelf()
person3.introduceSelf()
