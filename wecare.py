class Customer:

    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        self.__wallet_balance += amount

    def get_wallet_balance(self):
        return self.__wallet_balance


c1 = Customer(100, "Ahmed", 36, 1000000)

c1.set_wallet_balance(100000000000)

print(c1.get_wallet_balance())



