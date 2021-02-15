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

# References

[Read and Write to CSV](https://docs.python.org/3/library/csv.html)

[Get Dictionary Keys as list](https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/)

[The Pretty Table Library](https://pypi.org/project/prettytable/)

[Read and Write in JSON: Official Doc](https://docs.python.org/3/library/json.html#basic-usage)

[Read and write in JSON: Real Python](https://realpython.com/python-json/)
