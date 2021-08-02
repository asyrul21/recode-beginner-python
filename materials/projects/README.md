# Sample Project Solutions

In this folder, you will find the sample solutions to all the Project topics you can choose from:

- Birthday Tracker
- Quiz Game
- Inventory System
- Rock Scissors Paper game
- Tic Tac Toe Game
- TDEE Calculator

## Pre Requisites

Before running any of the projects, please make sure you have:

1. Installed Python
2. Installed a third party library called _prettytable_. If you have not, run:

```bash
pip install prettytable
```

3. If you are using the _CsvReadWriter_ class, make sure to specify the _encoding_ parameter, since Windows and MacOS both have their own default CSV encoding. Your `CsvReadWriter` should look like this:

```python
import csv

class CsvReadWriter:
    def __init__(self, filePath):
        self.file = filePath

    def load(self):
        data = []
        with open(self.file, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                data.append(row)
        return data

    def loadAsDictionary(self):
        data = []
        with open(self.file, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            for item in csv_reader:
                data.append(item)
        return data

    def save(self, data):
        fieldNames = data[0].keys()
        with open(self.file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldNames)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
```

## Running the Program

1. Navigate into the project you would like to run:

```bash
cd InventorySystem
```

2. Run the `app.py` file

```bash
python app.py
```

NOTE: Sometimes the file is called `game.py` or `tictactoe.py`. Just execute the Python file in the specific project's folder.

## Issues

If you encounter any issues, please let me know! And I will ammend the fixes the best way I can.
