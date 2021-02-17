# Lesson 8: Read and Write from External Files

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

# References

[Read and Write to CSV: RealPython](https://realpython.com/python-csv/)

[Read and Write to CSV: Official Doc](https://docs.python.org/3/library/csv.html)

[Get Dictionary Keys as list](https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/)

[The Pretty Table Library](https://pypi.org/project/prettytable/)

[Read and Write in JSON: Official Doc](https://docs.python.org/3/library/json.html#basic-usage)

[Read and write in JSON: Real Python](https://realpython.com/python-json/)
