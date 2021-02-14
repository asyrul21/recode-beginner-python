# Lesson 7: Classes, Objects and Dictionaries

## Classes

From `src/classes.py`

```python
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

```

Output:

```bash
My name is Bob Marley. I am 27 years old!
My name is Mike Tyson. I am 35 years old!
My name is Siti Aminah. I am 30 years old!
```

## Dictionary

From `src/dictionary.py`

```python
# defining a dictionary key-value pair

vehicleDictionary1 = {
    "type" : "car",
    "brand" : "Honda",
    "model" : "civic",
    "year": 2017
}

vehicleDictionary2 = {
    "type" : "motorcycle",
    "brand" : "BMW",
    "model" : "S1000",
    "year": 2012
}

print("Brand of vehicle: " + vehicleDictionary1["brand"])

print()
print("Add new data item in dictionary")
print()
vehicleDictionary1["owner"] = "Bob"
print(vehicleDictionary1)

print()
print("Remove data item in dictionary")
print()
vehicleDictionary1.pop("owner")
print(vehicleDictionary1)

print()
print("Edit data item in dictionary")
print()
vehicleDictionary1["year"] = 2020
print(vehicleDictionary1)

print()
print("Adding dictionaries into list")
print()
vehicleCollection = [vehicleDictionary1, vehicleDictionary2]
print(vehicleCollection)

print()
print("Remove all data items in dictionary")
print()
vehicleDictionary1.clear()
print(vehicleDictionary1)

```

Output:

```bash
Brand of vehicle: Honda

Add new data item in dictionary

{'type': 'car', 'brand': 'Honda', 'model': 'civic', 'year': 2017, 'owner': 'Bob'}

Remove data item in dictionary

{'type': 'car', 'brand': 'Honda', 'model': 'civic', 'year': 2017}

Edit data item in dictionary

{'type': 'car', 'brand': 'Honda', 'model': 'civic', 'year': 2020}

Adding dictionaries into list

[{'type': 'car', 'brand': 'Honda', 'model': 'civic', 'year': 2020}, {'type': 'motorcycle', 'brand': 'BMW', 'model': 'S1000', 'year': 2012}]

Remove all data items in dictionary

{}
```

## Combining Data Structures

From `src/combination.py`

```python
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
```

Output:

```bash
Puttiing person instances into a list:
Hi!
My name is Bob Marley. I am 27 years old!

Puttiing person instances into a dictionary:
Hi!
My name is Mike Tyson. I am 35 years old!
```

## Importing Data from External Files

### The JSON Format

From `src/data/students.json`

```json
[
  {
    "firstName": "Bob",
    "lastName": "Marley",
    "age": 27,
    "class": "Jupiter",
    "contact": {
      "home": "03787787787",
      "mobile": "0120120120"
    },
    "major": "Music"
  },
  {
    "firstName": "Mike",
    "lastName": "Tyson",
    "age": 35,
    "class": "Mars",
    "contact": {
      "home": "03787787787",
      "mobile": "0120120120"
    },
    "major": "Sports Science"
  },
  {
    "firstName": "Emma",
    "lastName": "Watson",
    "age": 41,
    "class": "Earth",
    "contact": {
      "home": "03787787787",
      "mobile": "0120120120"
    },
    "major": "Acting"
  }
]
```

Loading the Data, from `src/import.py`:

```python
import json
with open("data/students.json", "r") as read_file:
    data = json.load(read_file)

print()
print("First name of the 2nd student: " + data[1]["firstName"])
```

Making changes to the data:

```python
print()
print("Adding new entry to the data")

# creating a new student dictionary object
# or you can create a Student class and create new instance
newStudent = {
    "firstName": "James",
    "lastName": "Hetfield",
    "age": 35,
    "class": "Earth",
    "contact": {
      "home": "03787787787",
      "mobile": "0120120120"
    },
    "major": "Software Engineering"
}

data.append(newStudent)
print(data)
```

Saving the data back to json:

```python
print()
print("Saving the data back to JSON")

with open("students.json", "w") as write_file:
    json.dump(data, write_file)
    print("Saved successfully!)
```

NOTE: The _json.dump_ above generates an _UNFORMATTED_ json, meaning it appears as a single line. Don't worry about this, it is still JSON and will still work to store your data.

The updated JSON:

```json
[
  {
    "firstName": "Bob",
    "lastName": "Marley",
    "age": 27,
    "class": "Jupiter",
    "contact": { "home": "03787787787", "mobile": "0120120120" },
    "major": "Music"
  },
  {
    "firstName": "Mike",
    "lastName": "Tyson",
    "age": 35,
    "class": "Mars",
    "contact": { "home": "03787787787", "mobile": "0120120120" },
    "major": "Sports Science"
  },
  {
    "firstName": "Emma",
    "lastName": "Watson",
    "age": 41,
    "class": "Earth",
    "contact": { "home": "03787787787", "mobile": "0120120120" },
    "major": "Acting"
  },
  {
    "firstName": "James",
    "lastName": "Hetfield",
    "age": 35,
    "class": "Earth",
    "contact": { "home": "03787787787", "mobile": "0120120120" },
    "major": "Software Engineering"
  }
]
```

# Take Home Challenge

To successfully complete the Take Home Challenge, you first need to install prettyTable. Run the following command in your CLI:

```bash
pip install -U prettytable
```
