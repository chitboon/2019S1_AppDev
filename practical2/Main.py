import Phone as p
import Owner as o
dict = {}
while True:
   number = int(input('What is your desired phone number? '))
   if number in dict:
       print('This number is not available, please try again.')
       continue
   name = input('What is your name? ')
   owner = o.Owner(name)
   email = input('What is your email? ')
   owner.set_email(email)
   phone = p.Phone(number, owner)
   dict[phone.get_number()] = phone
   print('The number %d has been assigned to %s' % (phone.get_number(), owner.get_name()))
   check = input('Type q to quit the program: ')
   if check.lower() == 'q':
       break
