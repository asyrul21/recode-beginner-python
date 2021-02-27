from prettytable import PrettyTable
from .Utility import clearScreen

class TableDisplay:
    def __init__(self, fields):
        self.fields = fields
    
    def convertDictToRows(self, dataList):
        rows = []
        for item in dataList:
            row = []
            for field in self.fields:
                row.append(item[field])
            rows.append(row)
        return rows

    def display(self, dataList):
        table = PrettyTable()
        table.field_names = self.fields
        dataRows = self.convertDictToRows(dataList)
        table.add_rows(dataRows)
        table.align = "l"

        clearScreen()
        print("----------------------------------------------------------")
        print("\t\t    The Inventory System")
        print()
        print(table)
        print()