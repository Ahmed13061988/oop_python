class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.get_area(), self.address.get_door_no(), self.address.get_street(), self.address.get_pincode())

    def update_details(self, add):
        self.address = add


class Address:
    def __init__(self, door_no, street, area, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__area = area
        self.__pincode = pincode

    def set_door_no(self, door_no):
        self.__door_no = door_no

    def get_door_no(self):
        return self.__door_no

    def set_street(self, street):
        self.__street = street

    def get_street(self):
        return self.__street

    def set_area(self, area):
        self.__area = area

    def get_area(self):
        return self.__area

    def set_pincode(self, pincode):
        self.__pincode = pincode

    def get_pincode(self):
        return self.__pincode

    def update_address(self):
        pass


add1 = Address(105, "Harvard", "Aurora", 80014)
add2 = Address(107, "Mississippi", "Lakewood", 80231)

custom1 = Customer("Ahmed", 36, 7202438963, None)
custom1.update_details(add1)
custom1.view_details()


