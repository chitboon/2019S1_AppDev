import shelve

class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

def add_student():
    print('==== ADD ====')
    id = input("Enter student's id: ")
    name = input("Enter student's name: ")
    gpa = float(input("Enter student's gpa: "))
    student = Student(id, name, gpa)
    student_db = shelve.open('student_db')
    student_db[id] = student
    student_db.close()
    print("Student's Record Added")

def display_student():
    print('==== DISPLAY ====')
    student_db = shelve.open('student_db')
    for id in student_db:
        student = student_db[id]
        print(student.id, student.name, student.gpa)
    student_db.close()

def update_student():
    print('==== MODIFY ====')
    id = input("Enter student's id: ")
    student_db = shelve.open('student_db')
    if id in student_db:
        name = input("Enter student's name: ")
        gpa = input("Enter student's gpa: ")
        student = Student(id, name, gpa)
        student_db[id] = student
        print("Student's Record updated")
    else:
        print("ERROR: id does not exist")
    student_db.close()

def delete_student():
    print("==== DELETE ====")
    student_db = shelve.open('student_db')
    id = input("Enter student's id: ")
    if id in student_db:
        del student_db[id]
        print("Student's Record deleted")
    else:
        print("ERROR: id does not exist")
    student_db.close()

while True:
    print('==== Student Records ====')
    print('1.  Add Student record')
    print('2.  Display all students')
    print('3.  Update Student record')
    print('4.  Delete Student record')
    print('Q to quit')
    option = input('Please enter an option: ')
    if option == '1':
        add_student()
    elif option == '2':
        display_student()
    elif option == '3':
        update_student()
    elif option == '4':
        delete_student()
    elif option.upper() == 'Q':
        break
