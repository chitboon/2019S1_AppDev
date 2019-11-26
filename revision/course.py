class Course:
    def __init__(self, code, name, intake):
        self.__code = code
        self.__name = name
        self.__intake = intake

    def get_code(self):
        return self.__code

    def set_code(self, code):
        if len(code) == 6:
            self.__code = code
        else:
            print('Invalid course code')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_intake(self):
        return self.__intake

    def set_intake(self, intake):
        self.__intake = intake

course = Course('ITDF08', 'Diploma in Financial Informatics', 70)
print('The student intake for {}({}) is {}'.format(course.get_name(), course.get_code(), course.get_intake()))
