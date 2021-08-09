
class InventoryItem:
    def __init__(self, ID, name, category, quantity, desc):
        self.ID = ID
        self.name = name
        self.category = category
        self.quantity = quantity
        self.desc = desc

    def getDictionaryForm(self):
        return {
            "ID": str(self.ID),
            "Item": self.name,
            "Category" : self.category,
            "Quantity": int(self.quantity),
            "Description": self.desc
        }
