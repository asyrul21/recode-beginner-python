import json

class TxtReader:
    def __init__(self, filePath):
        self.file = filePath
        self.symbols = ['\n', '.', ',', '(', ')', '\'', ';', "\""]

    def load(self):
        with open(self.file, "r") as file:
            read_data = file.read()
            rawSentence = ""
            for chars in read_data:
                if(chars != '\n' and chars not in self.symbols):
                    rawSentence = rawSentence + chars

        return rawSentence
        







