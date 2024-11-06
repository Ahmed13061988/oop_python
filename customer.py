class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.area, self.address.street, self.address.door_no, self.address.pincode)

    def update_details(self, add):
        self.address = add


class Address:
    def __init__(self, door_no, street, area, pincode):
        self.door_no = door_no
        self.street = street
        self.area = area
        self.pincode = pincode

    def update_address(self):
        pass


add1 = Address(105, "Harvard", "Aurora", 80014)
add2 = Address(107, "Mississippi", "Lakewood", 80231)

custom1 = Customer("Ahmed", 36, 7202438963, None)
custom1.update_details(add1)
custom2 = Customer("Ali", 50, 234, add2)

custom1.view_details()

print(custom1.address.street)

