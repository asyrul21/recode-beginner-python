import csv

class CsvReadWriter:
    def __init__(self, filePath):
        self.file = filePath

    def load(self):
        data = []
        with open(self.file, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                data.append(row)
        return data

    def loadAsDictionary(self):
        data = []
        with open(self.file, "r") as csv_file:
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





