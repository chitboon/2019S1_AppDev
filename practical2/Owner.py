class Owner:
   def __init__(self, name):
       self.__name = name
       self.__email = ''
   def get_name(self):
       return self.__name
   def get_email(self):
       return self.__email
   def set_email(self, email):
       self.__email = email
   def set_name(self, name):
       self.__name = name
