class Customer:
    def __init__(self, name, age, phone_no, address, bill):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address
        self.bill = bill

    def purchase(self, payment):
        if payment.type == "card":
            print("Paying by card")
        elif payment.type == "cash":
            print("Paying by cash")

    def calculate_total(self):
        tax = Tax(self.cust_type)
        total_bill = self.bill * tax.x_details(self.cust_type)
        return total_bill

    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.get_area(), self.address.get_door_no(), self.address.get_street(),
              self.address.get_pincode())

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


class Payment:
    def __init__(self, type):
        self.type = type


class Tax:
    def __int__(self, cust_type):
        self.cust_type = cust_type

    def x_details(self, cust_type):
        if self.cust_type == "Student":
            return 5
        else:
            return 10


add1 = Address(105, "Harvard", "Aurora", 80014)
add2 = Address(107, "Mississippi", "Lakewood", 80231)

custom1 = Customer("Ahmed", 36, 7202438963, None, 600)
custom1.update_details(add1)
custom1.view_details()

custom3 = Customer("Ahmed", 36, 7202438963, add2, 500)

custom3.calculate_total()

p1 = Payment("card")

custom1.purchase(p1)
