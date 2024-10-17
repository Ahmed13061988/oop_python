class Item:
    pay_rate = 0.8  # Applying 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Validate the data type constructor received
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity}, is of wrong value"

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

print(Item.pay_rate)
