# Lesson 7 Part 1: Read and Write from External Files

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
    json.dump(data, write_file, indent=4)
    print("Saved successfully!)
```

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

### The CSV

From `src/solveTogether-ContactBookCSV/data/contactList.csv`

```csv
name,relation,home,mobile
Bob Marley,Brother,0311111111,01211111111
John Constantine,Cousin,0322222222,01222222222
Emma Watson,Sister,0333333333,01233333333
```

Loading the data. There are two ways you can do this. The first one is to use the generic reader.

From `src/solveTogether-ContactBookCSV/helper/CsvReadWriter`

```python
import csv

data = []
with open(self.file, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        data.append(row)
return data
```

This return your data as lists:

```bash
['name', 'relation', 'home', 'mobile']
['Bob Marley', 'Brother', '0311111111', '01211111111']
['John Constantine', 'Cousin', '0322222222', '01222222222']
['Emma Watson', 'Sister', '0333333333', '01233333333']
```

The other way is to use the `DictReader` which reads your data as dictionary. Personally, I prefer this one. However, it depends on your requirements whether or not to use either of these.

```python
data = []
with open(self.file, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    for item in csv_reader:
        data.append(item)
return data
```

Now, each item in the data list is a dictionary object. Just like how we were working with the JSON reader and writer.

Making changes to the data should be similar to how we did in JSON part above.

Saving data back to CSV:

```python
def save(self, data):
  fieldNames = data[0].keys()
  with open(self.file, 'w', newline='') as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames=fieldNames)
      writer.writeheader()
      for item in data:
          writer.writerow(item)
```

# Part 2: Introduction to Error Handling

## Example Problem 1: Division by 0

Without Exception Handling:

```python
number1 = input("Insert the first number: ")
number1 = float(number1)

number2 = input("What would you like to divide that number with?: ")
number2 = float(number2)

result = number1 / number2
print("Answer: " + str(result))
```

With Exception Handling, can be found in _exceptionHandling-1.py_:

```python
number1 = input("Insert the first number: ")
number1 = float(number1)

number2 = input("What would you like to divide that number with?: ")
number2 = float(number2)

try:
    result = number1 / number2
    print("Answer: " + str(result))
except Exception as err:
    print("Oops something went wrong. ERROR: " + str(err))
    print("Please make sure you are not performing division by 0")
```

Output:

```bash
Insert the first number: 100
What would you like to divide that number with?: 0
Oops something went wrong. ERROR: float division by zero
Please make sure you are not performing division by 0
```

## Example Problem 2: Getting and Invalid Input

Without Exception Handling:

```python
number1 = input("Insert a NUMBER: ")
number1 = float(number1)
```

With Exception Handling, can be found in _exceptionHandling-2.py_:

```python
try:
    number1 = input("Insert a NUMBER: ")
    number1 = float(number1)
    print("Success!")
except ValueError as valueErr:
    print("Oops something went wrong. Please input NUMBERS ONLY!")
    print("ERROR: " + str(valueErr))
except Exception as err:
    print("Oops the system failed.")
    print("ERROR: " + str(err))
```

Output:

```bash
Insert a NUMBER: haha
Oops something went wrong. Please input NUMBERS ONLY!
ERROR: could not convert string to float: 'haha'
```

## Reading and/or Writing to File

Without Exception Handling:

```python
import json
import pprint # https://docs.python.org/3/library/pprint.html
pp = pprint.PrettyPrinter(indent=4)

with open("data/students.json", "r") as read_file:
    data = json.load(read_file)

pp.pprint(data)
```

With Exception Handling, can be found in _exceptionHandling-3.py_ (SUCCESS)

```python
import json
import pprint # https://docs.python.org/3/library/pprint.html
pp = pprint.PrettyPrinter(indent=4)

try:
    with open("data/students.json", "r") as read_file:
        data = json.load(read_file)

    print("Read file success!")
    print("*********************")
    pp.pprint(data)
    print()
except IOError as ioerr:
    print("Failed to read file.")
    print("ERROR: " + str(ioerr))
except Exception as err:
    print("Oops something caused the program to crash and terminate")
    print("ERROR: " + str(err))
```

Output:

```bash
Read file success!
*********************
[   {   'age': 27,
        'class': 'Jupiter',
        'contact': {'home': '03787787787', 'mobile': '0120120120'},
        'firstName': 'Bob',
        'lastName': 'Marley',
        'major': 'Music'},
    {   'age': 35,
        'class': 'Mars',
        'contact': {'home': '03787787787', 'mobile': '0120120120'},
        'firstName': 'Mike',
        'lastName': 'Tyson',
        'major': 'Sports Science'},
    {   'age': 41,
        'class': 'Earth',
        'contact': {'home': '03787787787', 'mobile': '0120120120'},
        'firstName': 'Emma',
        'lastName': 'Watson',
        'major': 'Acting'},
    {   'age': 35,
        'class': 'Earth',
        'contact': {'home': '03787787787', 'mobile': '0120120120'},
        'firstName': 'James',
        'lastName': 'Hetfield',
        'major': 'Software Engineering'}]
```

With Exception Handling, can be found in _exceptionHandling-3.py_ (ERROR)

```python
import json
import pprint # https://docs.python.org/3/library/pprint.html
pp = pprint.PrettyPrinter(indent=4)

try:
    with open("data/studentsx.json", "r") as read_file:
        data = json.load(read_file)

    print("Read file success!")
    print("*********************")
    pp.pprint(data)
    print()
except IOError as ioerr:
    print("Failed to read file.")
    print("ERROR: " + str(ioerr))
except Exception as err:
    print("Oops something caused the program to crash and terminate")
    print("ERROR: " + str(err))
```

Output:

```bash
Failed to read file.
ERROR: [Errno 2] No such file or directory: 'data/studentsx.json'
```

# References

[Read and Write to CSV: RealPython](https://realpython.com/python-csv/)

[Read and Write to CSV: Official Doc](https://docs.python.org/3/library/csv.html)

[Get Dictionary Keys as list](https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/)

[The Pretty Table Library](https://pypi.org/project/prettytable/)

[Read and Write in JSON: Official Doc](https://docs.python.org/3/library/json.html#basic-usage)

[Read and write in JSON: Real Python](https://realpython.com/python-json/)

[Exception Handling Tutorial](https://docs.python.org/3/tutorial/errors.html)

[PPrint to pretty print data on command line](https://docs.python.org/3/library/pprint.html)
