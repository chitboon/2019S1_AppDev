class Employee:
    def __init__(self):
        self.__id =self.id = ''
        self.__name = ''
        self.__department = ''
        self.__title = ''

    def set_id(self, id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_department(self, dept):
        self.__department = dept
    def set_title(self, title):
        self.__title = title

    def __str__(self):
        return '{} (id={}) is a {} from {} department'.format(self.__name, self.__id, self.__title, self.__department)

e1 = Employee()
e1.set_id('jdee')
e1.set_name('Jay Dee')
e1.set_department('Sales')
e1.set_title('Manager')
# complete for the other 2 employee

print(e1)
# print the other 2 employees