import Person

class Student(Person.Person):
    def __init__(self, name, nric, admin_no):
        super().__init__(name, nric)
        self.__admin_no = admin_no
        self.__test_mark = 0
        self.__exam_mark = 0

    def get_admin_no(self):
        return self.__admin_no
    def get_test_mark(self):
        return self.__test_mark
    def get_exam_mark(self):
        return self.__exam_mark

    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no
    def set_test_mark(self, test_mark):
        self.__test_mark = test_mark
    def set_exam_mark(self, exam_mark):
        self.__exam_mark = exam_mark

    def computeFinalMark(self):
        return (self.__test_mark + self.__exam_mark) / 2

    def __str__(self):
        s = super().__str__()
        s = s+  ' Name: %s, Admin No: %s, Final Mark: %.2f' %(self.get_name(), self.get_admin_no(), self.computeFinalMark())
        return s