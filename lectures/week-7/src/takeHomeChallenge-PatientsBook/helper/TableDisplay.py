from prettytable import PrettyTable
import os

class TableDisplay:
    def __init__(self, fields):
        self.fields = fields
    
    def _convertDictToRows(self, dataList):
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
        dataRows = self._convertDictToRows(dataList)
        table.add_rows(dataRows)
        table.align = "l"

        os.system("clear")
        print("----------------------------------------------------------")
        print("\t\t    Patients Book App")
        print()
        print(table)
        print()