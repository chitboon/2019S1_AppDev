class Phone:
    count = 0
    def __init__(self, number, owner):
        self.__number = number
        self.__owner = owner
        self.__class__.count +=1
    def get_number(self):
        return self.__number
    def get_owner(self):
        return self.__owner
    def set_number(self, number):
        self.__number = number
    def set_owner(self, owner):
        self.__owner = owner