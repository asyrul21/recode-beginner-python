import pandas as pd

print("Pandas Demo!")

studentsDataFrame = pd.read_csv("data/csv/students.csv", delimiter=",", index_col=0)
studentsDataFrame.index.name = None

parentsDataFrame = pd.read_csv("data/csv/parents.csv", delimiter=",", index_col=0)
parentsDataFrame.index.name = None

addressesDataFrame = pd.read_csv("data/csv/addresses.csv", delimiter=",", index_col=0)
addressesDataFrame.index.name = None

# print(studentsDataFrame)
# print(parentsDataFrame)
# print(addressesDataFrame)

# marksColumn = studentsDataFrame["Marks"]
# print(marksColumn)

# filteredStudentsDf = studentsDataFrame.drop(columns=["Name"])
# print(filteredStudentsDf)

# filteredStudentDf2 = studentsDataFrame.filter(items=["Marks", "Group", "Height(m)"])
# print(filteredStudentDf2)

# studentsFromMercury = studentsDataFrame[(studentsDataFrame["Group"] == "Mercury")]
# print(studentsFromMercury)

# studentsFromMercuryAndEarth = studentsDataFrame[
#     (studentsDataFrame["Group"] == "Mercury") | (studentsDataFrame["Group"] == "Earth")]
# print(studentsFromMercuryAndEarth)

# studentsInMercuryScoringAnA = studentsDataFrame[(studentsDataFrame["Group"] == "Mercury") & (studentsDataFrame["Marks"] < 50)]

# print("Mercury students who failed the test:")
# print(studentsInMercuryScoringAnA)

# groupByClass = studentsDataFrame.groupby(["Group"]).max()
# groupByClassFiltered = groupByClass.filter(items=["Group", "Marks"])
# print(groupByClassFiltered)

# print(studentsDataFrame)

studentsAndAddresses = studentsDataFrame.join(addressesDataFrame)
# groubByCountry = studentsAndAddresses.groupby(["country"])
# groubByCountryCount = groubByCountry.agg(
#     Count=("address", "count")
# )
# print(groubByCountryCount)

studentsAndAddresses.to_csv("data/csv/result_csv.csv", index=True)
print("Saved successfully!")

