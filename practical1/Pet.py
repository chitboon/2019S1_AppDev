class Pet:
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = 0

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        s = 'Pet {} is a {}, and it is {} years old'.format(self.get_name(), self.get_animal_type(),self.get_age())
        return s


name = input('Enter pet name: ')
type = input('Enter pet type: ')
age = int(input('Enter age of pet: '))
pet = Pet()
pet.set_name(name)
pet.set_animal_type(type)
pet.set_age(age)
print('Pet %s is a %s, and it is %d years old' % (pet.get_name(), pet.get_animal_type(),pet.get_age()))
print(pet)
