from datetime import date, datetime
from config import DATE_FORMAT

class Birthdate:
    def __init__(self, ID, name, relation, birthdate):
        self.ID = ID
        self.name = name
        self.relation = relation
        self.birthdateRaw = birthdate
        self.birthdateObject = self.convertToDateObject(birthdate)
        self.birthdateString = self.convertDateObjectToString(self.birthdateObject)

    def convertToDateObject(self, dateString):
        return datetime.strptime(dateString, DATE_FORMAT)

    def convertDateObjectToString(self, dateObject):
        return datetime.strftime(dateObject, DATE_FORMAT)

    def getDictionaryForm(self):
        return {
            "ID": self.ID,
            "name": self.name,
            "relation": self.relation,
            "birthdate": self.birthdateString
        }

    
