import Person

class Lecturer(Person.Person):
    def __init__(self, name, nric, staff_id, total_teaching_hr):
        super().__init__(name, nric)
        self.__staff_id = ""
        self.set_staff_id(staff_id)
        self.__total_teaching_hour = total_teaching_hr

    def get_staff_id(self):
        return self.__staff_id
    def get_total_teaching_hour(self):
        return self.__total_teaching_hour
    def set_staff_id(self, staff_id):
        if self.get_nric() == staff_id:
            self.__staff_id = staff_id
        else:
            print("Not the same")

    def set_total_teaching_hour(self, total_teaching_hr):
        self.__total_teaching_hour = total_teaching_hr

    def computeSalary(self):
        return self.__total_teaching_hour*90
