class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)


item2 = Item("Laptop", 1000, 5)

item2.has_numpad = False
