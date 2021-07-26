import pandas as pd

# import data as DataFrames
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

studentsDataFrame = pd.read_csv("data/csv/students.csv", delimiter=",", index_col=0)
studentsDataFrame.index.name = None

parentsDataFrame = pd.read_csv("data/csv/parents.csv", delimiter=",", index_col=0)
parentsDataFrame.index.name = None

addressesDataFrame = pd.read_csv("data/csv/addresses.csv", delimiter=",", index_col=0)
addressesDataFrame.index.name = None

print("Students:")
print(studentsDataFrame)
print()
print("Parents:")
print(parentsDataFrame)
print()
print("Addresses:")
print(addressesDataFrame)

# column filter
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html

filteredStudents = studentsDataFrame.drop(columns=["Name"])
print()
print("Students with filtered columns:")
print(filteredStudents)
print()
print("View a single column:")
print(filteredStudents["Marks"])

# simple row filter
studentsInMercury = studentsDataFrame[(studentsDataFrame["Group"] == "Mercury")]

print()
print("Students in Mercury Class:")
print(studentsInMercury)

# multi-condition row filter
# use & or |
studentsInMercuryAndEarth = studentsDataFrame[
    (studentsDataFrame["Group"] == "Mercury") | (studentsDataFrame["Group"] == "Earth")]

print()
print("Students in Mercury and Earth Class:")
print(studentsInMercuryAndEarth)

studentsInMercuryWhoScoredA = studentsDataFrame[
    (studentsDataFrame["Group"] == "Mercury") & (studentsDataFrame["Marks"] > 80)]

print()
print(str(len(studentsInMercuryWhoScoredA.index)) + " student(s) scored an A.")
print("Students in Mercury who score an A:")
print(studentsInMercuryWhoScoredA)

studentsInMercuryWhoFailed = studentsDataFrame[
    (studentsDataFrame["Group"] == "Mercury") & (studentsDataFrame["Marks"] < 50)]

print()
print(str(len(studentsInMercuryWhoFailed.index)) + " student(s) failed the test.")
print("Students in Mercury who failed:")
print(studentsInMercuryWhoFailed)

# group by and perform average
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
groupByAverage = studentsDataFrame.groupby(["Group"]).mean()
groupByAverage.index.name = None
# select relevant columns
averageMarksByClass = groupByAverage.filter(items=["Group", "Marks"])

print()
print("Average marks, grouped by Class")
print(averageMarksByClass)

# group by and get max score
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
groupByAverage = studentsDataFrame.groupby(["Group"]).max() 
# for mininum, use .min(), for sum, use .sum()
groupByAverage.index.name = None
# select relevant columns
highestMarksByClass = groupByAverage.filter(items=["Group", "Marks"])

print()
print("Highest marks, grouped by Class")
print(highestMarksByClass)

# joining 2 dataframes
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html
# ID's must match
# to join manually on custom keys, use the "on" optional argument

# set pandas to show all columns
pd.set_option("display.max_columns", None)
pd.set_option('display.expand_frame_repr', False)

studentsAndAddress = studentsDataFrame.join(addressesDataFrame)

# drop unwanted columns
studentsAndAddress = studentsAndAddress.drop(columns=["state", "Gender", "Height(m)"])

print()
print("Students and addresses:")
print(studentsAndAddress)

# count students by nationality

studentsByCountryCount = studentsAndAddress.groupby(["country"])
# select relevant columns using named aggregation
studentsByCountry = studentsByCountryCount.agg(
    count=("address", "count")
)

print()
print("Students by Country:")
print(studentsByCountry)

# save result as json
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html

studentsAndAddress.to_json("data/json/result_json.json", orient="records", indent=4)

# save result as csv
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

studentsAndAddress.to_csv("data/csv/result_csv.csv", index=True)


