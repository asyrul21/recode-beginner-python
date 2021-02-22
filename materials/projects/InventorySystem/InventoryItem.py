
class InventoryItem:
    def __init__(self, ID, name, category, quantity, desc):
        self.ID = ID
        self.item = name
        self.category = category
        self.quantity = quantity
        self.description = desc
        self.dictionaryForm = self._getDictionaryForm()

    def _getDictionaryForm(self):
        return {
            "ID": str(self.ID),
            "Item": self.item,
            "Category": self.category,
            "Quantity": self.quantity,
            "Description": self.description,
        }

    
