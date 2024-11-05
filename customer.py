class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        pass

    def update_details(self):
        pass


class Address:
    def __init__(self, door_no, street, area, pincode):
        self.door_no = door_no
        self.street = street
        self.area = area
        self.pincode = pincode

    def update_address(self):
        pass
