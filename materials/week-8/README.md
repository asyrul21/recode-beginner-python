# Lesson 8: Introduction to Libraries, Pandas

## Setup

1. Make sure you have installed `pandas`. To see all installed third party libraries, run:

```bash
conda list
```

2. You will see `pandas` in one of the items

3. If you don't, or you haven't installed it, do:

```bash
conda install pandas
```

## Importing in Your Python Code

```python
import pandas as pd
```

## Using Pandas

### Reading a CSV File

Doc: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

```python
studentsDataFrame = pd.read_csv("data/csv/students.csv", delimiter=",", index_col=0)
studentsDataFrame.index.name = None

print("Students:")
print(studentsDataFrame)
print()
```

Result:

```bash
Students:
              Name Gender  Age  Marks    Group  Height(m)
1     John Marston      M   12     72  Mercury        1.6
2          Fatimah      F   11     85  Mercury        1.5
3     Muhammad Ali      M   12     65    Earth        1.4
4       Usain Bolt      M   10     75     Mars        1.3
5      Emma Watson      F   12     88     Mars        1.5
6       Abdul Aziz      M   12     92     Mars        1.6
7        Tom Hanks      M   10     81    Earth        1.5
8   Dwayne Johnson      M   12     42  Mercury        1.6
9      Siti Aishah      F   10     66     Mars        1.2
10       Bob Dylan      M   10     32    Earth        1.4

```

### Selecting/Viewing Specific Columns

```python
marks = filteredStudents["Marks"]

print("View a single column:")
print(marks)
```

Result:

```bash
View a single column:
1     72
2     85
3     65
4     75
5     88
6     92
7     81
8     42
9     66
10    32
Name: Marks, dtype: int64
```

### Filter Unwanted Columns

Doc: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html

```python
filteredStudents = studentsDataFrame.drop(columns=["Name"])

print()
print("Students with filtered columns:")
print(filteredStudents)
print()
```

Result:

```bash
Students with filtered columns:
   Gender  Age  Marks    Group  Height(m)
1       M   12     72  Mercury        1.6
2       F   11     85  Mercury        1.5
3       M   12     65    Earth        1.4
4       M   10     75     Mars        1.3
5       F   12     88     Mars        1.5
6       M   12     92     Mars        1.6
7       M   10     81    Earth        1.5
8       M   12     42  Mercury        1.6
9       F   10     66     Mars        1.2
10      M   10     32    Earth        1.4
```

### Row Filter by Value

Show only students from Mercury group

```python
studentsInMercury = studentsDataFrame[(studentsDataFrame["Group"] == "Mercury")]

print()
print("Students in Mercury Class:")
print(studentsInMercury)
```

Result:

```bash
Students in Mercury Class:
             Name Gender  Age  Marks    Group  Height(m)
1    John Marston      M   12     72  Mercury        1.6
2         Fatimah      F   11     85  Mercury        1.5
8  Dwayne Johnson      M   12     42  Mercury        1.6
```

Show only students from Mercury and Eath Groups

```python
studentsInMercuryAndEarth = studentsDataFrame[
    (studentsDataFrame["Group"] == "Mercury") | (studentsDataFrame["Group"] == "Earth")]

print()
print("Students in Mercury and Earth Class:")
print(studentsInMercuryAndEarth)
```

Result:

```bash
Students in Mercury and Earth Class:
              Name Gender  Age  Marks    Group  Height(m)
1     John Marston      M   12     72  Mercury        1.6
2          Fatimah      F   11     85  Mercury        1.5
3     Muhammad Ali      M   12     65    Earth        1.4
7        Tom Hanks      M   10     81    Earth        1.5
8   Dwayne Johnson      M   12     42  Mercury        1.6
10       Bob Dylan      M   10     32    Earth        1.4
```

Show students in Mercury Group who scored an A

```python
studentsInMercuryWhoScoredA = studentsDataFrame[
    (studentsDataFrame["Group"] == "Mercury") & (studentsDataFrame["Marks"] > 80)]

print()
print(str(len(studentsInMercuryWhoScoredA.index)) + " student(s) scored an A.")
print("Students in Mercury who score an A:")
print(studentsInMercuryWhoScoredA)
```

Result:

```bash
1 student(s) scored an A.
Students in Mercury who score an A:
      Name Gender  Age  Marks    Group  Height(m)
2  Fatimah      F   11     85  Mercury        1.5
```

Show students in Mercury group who failed the test

```python
studentsInMercuryWhoFailed = studentsDataFrame[
    (studentsDataFrame["Group"] == "Mercury") & (studentsDataFrame["Marks"] < 50)]

print()
print(str(len(studentsInMercuryWhoFailed.index)) + " student(s) failed the test.")
print("Students in Mercury who failed:")
print(studentsInMercuryWhoFailed)
```

Result:

```bash
1 student(s) failed the test.
Students in Mercury who failed:
             Name Gender  Age  Marks    Group  Height(m)
8  Dwayne Johnson      M   12     42  Mercury        1.6
```

### Grouping Data and Peforming Aggregation Operations

Doc: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

Get average marks by Class

```python
groupByAverage = studentsDataFrame.groupby(["Group"]).mean()
groupByAverage.index.name = None
# select relevant columns
averageMarksByClass = groupByAverage.filter(items=["Group", "Marks"])

print()
print("Average marks, grouped by Class")
print(averageMarksByClass)
```

Result:

```bash
Average marks, grouped by Class
             Marks
Earth    59.333333
Mars     80.250000
Mercury  66.333333
```

Get highest marks, group by class

```python
groupByAverage = studentsDataFrame.groupby(["Group"]).max()
# for mininum, use .min(), for sum, use .sum()
groupByAverage.index.name = None
# select relevant columns
highestMarksByClass = groupByAverage.filter(items=["Group", "Marks"])

print()
print("Highest marks, grouped by Class")
print(highestMarksByClass)
```

Result:

```bash
Highest marks, grouped by Class
         Marks
Earth       81
Mars        92
Mercury     85
```

### Joining 2 DataFrames by Column

DOC: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html

- ID's must match

- to join manually on custom keys, use the "on" optional argument

```python
studentsAndAddress = studentsDataFrame.join(addressesDataFrame)
# drop unwanted columns
studentsAndAddress = studentsAndAddress.drop(columns=["state", "Gender", "Height(m)"])

print()
print("Students and addresses:")
print(studentsAndAddress)
```

Result:

```bash
Students and addresses:
              Name  Age  Marks    Group                            address    country
1     John Marston   12     72  Mercury                     23 jalan 22/99   Malaysia
2          Fatimah   11     85  Mercury  2 jalan baru 45 Bandar Baru Bangi   Malaysia
3     Muhammad Ali   12     65    Earth             23 Thomas Road Bangsar   Malaysia
4       Usain Bolt   10     75     Mars       7 jalan tembok Seberang Prai   Malaysia
5      Emma Watson   12     88     Mars              1 New Road, Nice City  Singapore
6       Abdul Aziz   12     92     Mars     5 jalan batu tiga, Subang Jaya   Malaysia
7        Tom Hanks   10     81    Earth                31-2 Top Residences  Indonesia
8   Dwayne Johnson   12     42  Mercury           12-1-14 Beauty Apartment  Singapore
9      Siti Aishah   10     66     Mars      17 Motorcycle Rd, Bukit Batok  Singapore
10       Bob Dylan   10     32    Earth                   8 Jalan Soekarno  Indonesia
```

Count students by Nationality

```python
studentsByCountryCount = studentsAndAddress.groupby(["country"])
# select relevant columns using named aggregation
studentsByCountry = studentsByCountryCount.agg(
    count=("address", "count")
)

print()
print("Students by Country:")
print(studentsByCountry)
```

Result:

```bash
Students by Country:
           count
country
Indonesia      2
Malaysia       5
Singapore      3
```

### Saving Data to JSON

DOCS: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html

```python
studentsAndAddress.to_json("data/json/result_json.json", orient="records", indent=4)
```

_result_json.json_:

```json
[
    {
        "Name":"John Marston",
        "Gender":"M",
        "Age":12,
        "Marks":72,
        "Group":"Mercury",
        "Height(m)":1.6,
        "address":"23 jalan 22\/99",
        "state":"Selangor",
        "country":"Malaysia"
    },
    {
        "Name":"Fatimah",
        "Gender":"F",
        "Age":11,
        "Marks":85,
        "Group":"Mercury",
        "Height(m)":1.5,
        "address":"2 jalan baru 45 Bandar Baru Bangi",
        "state":"Selangor",
        "country":"Malaysia"
    },
    {
        "Name":"Muhammad Ali",
        "Gender":"M",
        "Age":12,
        "Marks":65,
        "Group":"Earth",
        "Height(m)":1.4,
        "address":"23 Thomas Road Bangsar",
        "state":"Kuala Lumpur",
        "country":"Malaysia"
    },

    ...
]
```

### Saving Data to CSV

DOCS: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

```python
studentsAndAddress.to_csv("data/csv/result_csv.csv", index=True)
```

_result_csv.csv_ :

```csv
,Name,Gender,Age,Marks,Group,Height(m),address,state,country
1,John Marston,M,12,72,Mercury,1.6,23 jalan 22/99,Selangor,Malaysia
2,Fatimah,F,11,85,Mercury,1.5,2 jalan baru 45 Bandar Baru Bangi,Selangor,Malaysia
3,Muhammad Ali,M,12,65,Earth,1.4,23 Thomas Road Bangsar,Kuala Lumpur,Malaysia

...
```
