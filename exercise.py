class Freight:

    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.recipient_customer = recipient_customer
        self.from_customer = from_customer
        self.weight = weight
        self.distance = distance
        self.counter = 198
        self.freight_id = 0
        self.freight_charge = 0

    def validate_weight(self, weight):
        if weight % 5 == 0:
            return True
        else:
            return False

    def validate_distance(self, distance):
        if distance < 5000 or distance > 500:
            return True
        else:
            return False

    def validate_customer_id(self, cust_id):
        if len(cust_id) == 6 and cust_id[0] == "1":
            return True
        else:
            return False

    def forward_cargo(self):
        if self.validate_customer_id and self.validate_distance and self.validate_weight:
            self.freight_id = 200
            self.freight_charge = self.weight * self.distance
        else:
            self.freight_charge = 0


class Customer:
    def __int__(self, customer_id, customer_name, address):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.address = address
