import pandas as pd

# set pandas to show all columns
pd.set_option("display.max_columns", None)
pd.set_option('display.expand_frame_repr', False)

# For this week's end of class, given the data files, you need to perform
# simple data analytics using Pandas to answer a few  Analysis questions:
# 1. What is the average height of all the students joining from Malaysia?
# 2. list down the names of students, together with their parents'. To do this, you may
#   need to join your students data frame with the "parents.csv" data frame. Use the Github #   notes to help you!
# 3. Finally, you need to deliver gifts to all your students scoring an A, but only for
#   those living in Malaysia.
#   List down the names, their marks, their addresses, their parents' names, and
#   their contact numbers of these students, to help you with the shipping work. Also,
#   don't forget to save this resulting data back as a CSV! Name this file as result.csv
#   TIP: You may need to perform more than one Joins!

studentsDataFrame = pd.read_csv("data/csv/students.csv", delimiter=",", index_col=0)
studentsDataFrame.index.name = None

parentsDataFrame = pd.read_csv("data/csv/parents.csv", delimiter=",", index_col=0)
parentsDataFrame.index.name = None

addressesDataFrame = pd.read_csv("data/csv/addresses.csv", delimiter=",", index_col=0)
addressesDataFrame.index.name = None

print()
print("Average height of all students from Malaysia")

studentsAndAddress = studentsDataFrame.join(addressesDataFrame)
groupedStudentsAndAddress = studentsAndAddress.groupby("country").mean()
filteredStudentsAndAddress = groupedStudentsAndAddress.filter(items=["country", "Height(m)"])

print(filteredStudentsAndAddress)

studentsAndParents = studentsDataFrame.join(parentsDataFrame)
studentAndParentsNames = studentsAndParents.filter(items=["Name", "parentName"])

print()
print("Students and their parents' names")
print(studentAndParentsNames)

joinedDataFrame = studentsAndParents.join(addressesDataFrame)
filteredJoinedDf = joinedDataFrame[(joinedDataFrame["Marks"] > 80) & (joinedDataFrame["country"] == "Malaysia")]
resultDf = filteredJoinedDf.filter(items=["Name", "Marks", "address", "parentName", "contact"])

print()
print("Result:")
print(resultDf)# save to csv

resultDf.to_csv("data/csv/result_csv.csv", index=True)

print()
print("Result saved successfully.")