class Item:
    pay_rate = 0.8  # Applying 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0, all=[]):
        # Validate the data type constructor received
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity}, is of wrong value"
        all.append(self)

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  # Using self instead of class itself will be better practice, when we want to change the class variable to specific
        # class instance


item1 = Item("Phone", 100, 5)

# print(item1.calculate_total())

item2 = Item("Laptop", 1000, 5)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

item2.has_numpad = False

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# item1.apply_discount()
# print(item1.price)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
print(self.all)
