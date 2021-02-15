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

<br/>

# Take Home Challenge

There are two challenges, each is it's own containing application:

1. The Patients Book Application

2. The Text File word counter

## The Patients Book

To successfully complete the Take Home Challenge, you first need to install the `prettyTable` library. Run the following command in your CLI:

```bash
pip install -U prettytable
```

Read more on the Pretty Table Library here: [The Pretty Table Library](https://pypi.org/project/prettytable/)

### Helper Classes

To assist your completion of this challenge, I have written Three(3) helper classes to help you load, write and print data. These classes can be found in `src/takeHomeChallenge-PatientsBook/helper`. I strongly advice that you DO NOT MODIFY ANY OF THE CODE IN HERE.

All three of these classes HAVE ALREADY BEEN INSTANTIATED AND INITIALIZED AT THE TOP OF YOU `app.py` file. From `src/takeHomeChallenge-PatientsBook/app.y`:

```python
# do not modify the code in here ##############################
from helper.JsonReadWriter import JsonReadWriter
from helper.TableDisplay import TableDisplay
from helper.NavigationDisplay import NavigationDisplay

DATA_PATH_JSON = "data/patients.json"

# load data
jsonRW = JsonReadWriter(DATA_PATH_JSON)
data = jsonRW.load()

# create display instance
tableDisplay = TableDisplay(data[0].keys())
navDisplay = NavigationDisplay()
# do not delete the code in here ##############################
###############################################################
```

These 3 classes are:

1. The `JsonReadWrite`. This class is meant to help you with _READING_ data from a JSON file, and to _WRITE_ or SAVE your data back to the JSON file.

   NOTE: WE WILL LEARN ABOUT DATA FILE READ AND WRITE NEXT WEEK

   The class has been instantiated to an object called `jsonRW`. Hence, ot use any of its methods, you need to reference the OBJECT. DONT reference to BLUEPRINT. Example:

   ```python
   jsonRW.save(data)
   ```

   The class has two methods:

   - `load()` : To convert data from json files to the Python Data Structures. You do not need to care much about this method because it is only executed once. This method returns a LIST OF DICTIONARIES containing the data. The `data` now contains this:

   ```bash
   [
       {
           "fullnName": "Bob Marley",
           "birthdate": "15/3/1950",
           "contact": "01211111111",
           "lastVisitDate": "14/1/2021",
           "lastVisitDescription": "Fever.",
           "lastVisitPrescription": "500mg Paracetamol."
       },
       {
           "fullnName": "Siti Aminah",
           "birthdate": "5/2/1975",
           "contact": "01222222222",
           "lastVisitDate": "3/1/2021",
           "lastVisitDescription": "Allergy reaction. Rashes on skin.",
           "lastVisitPrescription": "Cetrizine tablets."
       },
       {
           "fullnName": "Dwayne Johnson",
           "birthdate": "21/4/1984",
           "contact": "0123333333",
           "lastVisitDate": "2/2/2021",
           "lastVisitDescription": "Broken right arm.",
           "lastVisitPrescription": "Applied bandages."
       }
   ]
   ```

   - `save()` : This method saves the updated data back to the JSON file, enabling Data Persistence. This means that, even when you close and exit your app, the data remains. You will need to call this method after your have made modifications to the original `data` variable. It takes a list of Dictionaries similar to the one above as an argument.

2. The `TableDisplay` class. This class simply displays the data in a nice table to the screen. The class has been instantiated to an object named `tableDisplay`. To use any of its methods, reference the OBJECT. Example:

   ```python
   tableDisplay.display(data)
   ```

   The class only has 1 public method, the `display()`. The method simply takes a list of data as an argument.

   IMPORTANT NOTE:

   For this method to work properly, the attributes of each data item MUST be the same. Therefore, when you add new data to the `data` list, create a Patient class first, to encapsulate the field names. Then, create a new Patient instance containing new data. Now the data is a Patient object. To convert this to a dictionary, use the `__dict__` object instance variable. Once you have the dictionary form of the new data, append it to the `data` list.

   Example:

   ```python
   # create new patient instance
   newPatient = Patient(fullName, birthdate, contact, lastVisitDate, lastVisitDescription, lastVisitTreatment)

   # add the dictionary form to the data list
   data.append(newPatient.__dict__)
   ```

3. The `NavigationDisplay` class. This class simply print to the screen navigational information, for the users to choose, like a menu. You may need to LOOK into this method to see what are the available functionalitites. However you DO NOT have to make changes.

   There are 2 _void_ methods which you can access from the instantiated object `navDisplay`:

   - `printMainMenu()` which prints the navigational choices

   - `printExit()` which prints a goodbye to the user

### Execution

1. Follow the instructions in `src/takeHomeChallenge-PatientsBook/app.py`

2. Run your code by typing

   ```python
   python app.py
   ```

3. Your output should look something like this:

   ```bash
    ----------------------------------------------------------
   	    Patients Book App

    +----------------+-----------+-------------+---------------+----------------------+--------------------+
    |    fullName    | birthdate |   contact   | lastVisitDate | lastVisitDescription | lastVisitTreatment |
    +----------------+-----------+-------------+---------------+----------------------+--------------------+
    |   Bob Marley   | 15/3/1950 | 01211111111 |   14/1/2021   |        Fever.        | 500mg Paracetamol. |
    |  Siti Aminah   |  5/2/1975 | 01222222222 |    3/1/2021   |   Rashes on skin.    | Cetrizine tablets. |
    | Dwayne Johnson | 21/4/1984 |  0123333333 |    2/2/2021   |  Broken right arm.   | Applied bandages.  |
    +----------------+-----------+-------------+---------------+----------------------+--------------------+

    --------------------------------------------
    Activity			        | Selection
    --------------------------------------------
    Create new contact		    |	1
    Search for Contact by Name	|	2
    Exit				        |	3
    --------------------------------------------

    What would you like to do? :
   ```

   ```bash
   What would you like to do? : 2
   Insert name to search for: mar
   ```

   ```bash
    ----------------------------------------------------------
                Patients Book App

    +------------+-----------+-------------+---------------+----------------------+--------------------+
    |  fullName  | birthdate |   contact   | lastVisitDate | lastVisitDescription | lastVisitTreatment |
    +------------+-----------+-------------+---------------+----------------------+--------------------+
    | Bob Marley | 15/3/1950 | 01211111111 |   14/1/2021   |        Fever.        | 500mg Paracetamol. |
    +------------+-----------+-------------+---------------+----------------------+--------------------+

    Press any key to continue
   ```
