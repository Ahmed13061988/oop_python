class CustomerCare:
    __help_line = 9112

    @classmethod
    def get_helpline(cls):
        return cls.__help_line


class Customer:
    def call_support(self):
        print("Calling", CustomerCare.get_helpline())


customer1 = Customer()
customer1.call_support()
