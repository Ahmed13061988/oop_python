class Student:

    def __init__(self, stud_id=None, age=None, marks=None, course_id=None, fees=None):
        self.fees = None
        self.course_id = None
        self.stud_id = None
        self.age = None
        self.marks = None

    courses = {1001: 25575.0, 1002: 15500.0}

    def set_stud_id(self, stud_id):
        self.stud_id = stud_id

    def get_stud_id(self):
        return self.stud_id

    def set_course_id(self, course_id):
        self.course_id = course_id

    def get_course_id(self):
        return self.course_id

    def set_fees(self, fees):
        self.fees = fees

    def get_fees(self):
        return self.fees

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks

    def validate_marks(self):
        if self.marks >= 65:
            return True
        else:
            return False

    def validate_age(self):
        if self.age > 20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            return True
        else:
            return False

    def choose_course(self, course_id):
        if s1.check_qualification() and course_id in Student.courses:
            self.course_id = course_id
            if self.marks > 85:
                self.fees = Student.courses[course_id] * 0.75
                print(self.fees)
            else:
                self.fees = Student.courses[course_id]
                print(self.fees)  
            return True
        else:
            return False


s1 = Student()
s1.set_stud_id(1001)
s1.set_age(21)
s1.set_marks(90)

s1.validate_age()
s1.validate_marks()
# print(s1.check_qualification())
print(s1.choose_course(1001))
