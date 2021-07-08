print("Importing students.json")

import json
with open("data/students.json", "r") as read_file:
    data = json.load(read_file)

print()
print("First name of the 2nd student: " + data[1]["firstName"])

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
print(data[len(data) - 1])

# print()
print("Saving the data back to JSON")

with open("data/students.json", "w") as write_file:
    # jsonString = json.dumps(data, indent=4)
    # print(jsonString)
    json.dump(data, write_file)
    print("Saved successfully!")