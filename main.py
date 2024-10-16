class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Validate the data type constructor received
        assert price >= 0
        assert quantity >= 0

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)

print(item1.calculate_total())

item2 = Item("Laptop", 1000, 5)

item2.has_numpad = False
