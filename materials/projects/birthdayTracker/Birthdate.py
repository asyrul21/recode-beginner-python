from datetime import datetime
DATE_FORMAT = "%d/%m/%Y"

class Birthdate:
    def __init__(self, ID, name, relation, birthdate):
        self.ID = ID
        self.name = name
        self.relation = relation
        self.birthdateRaw = birthdate
        self.birthdateObject = self.convertToDateObj(birthdate)
        self.birthdateString = self.convertDatObjToString(self.birthdateObject)

    def convertToDateObj(self, dateString):
        return datetime.strptime(dateString, DATE_FORMAT)

    def convertDatObjToString(self, dateObj):
        return datetime.strftime(dateObj, DATE_FORMAT)

    def getBirthdateString(self):
        return self.birthdateString

    def getBirthdateObject(self):
        return self.birthdateObject

    def getDictionaryForm(self):
        return {
            "ID": self.ID,
            "name": self.name,
            "relation": self.relation,
            "birthdate": self.birthdateString
        }