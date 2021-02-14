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
