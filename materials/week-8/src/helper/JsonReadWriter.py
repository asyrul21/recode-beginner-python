import json

class JsonReadWriter:
    def __init__(self, filePath):
        self.file = filePath

    def load(self):
        data = []
        try:
            with open(self.file, "r") as read_file:
                data = json.load(read_file)
                return data
        except IOError as err:
            print("File reading failed!")
            print(str(err))

    def save(self, data):
        print("Saving the data...")
        with open(self.file, "w") as write_file:
            json.dump(data, write_file, indent=4)
            print("Saved successfully to " + self.file)





