class Person:
    def __init__(self, email, firstname, lastname):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return self.firstname + ' ' + self.lastname

# Part (a) Create Instructor class, initializer and methods
class Instructor(Person):
    def __init__(self, email, firstname, lastname):
        super().__init__(email, firstname, lastname)
        self.students = {}

    def get_name(self):
        return self.firstname + ' ' + self.lastname + '(Instructor)'

    def add_student(self, student):
#        if isinstance(student, Student):
        self.students[student.email] = student

class Student(Person):
    def __init__(self, email, firstname, lastname):
        super().__init__(email,firstname,lastname)
        self.group = ''



# Part (c) Implement load_students() Function
def load_students():
    student_list = []
    try:
        f = open('student.txt', 'r')

        for s in f:
            # firstname, lastname, email
            list = s.split(',')
            student = Student(list[2],list[0],list[1])
            student_list.append(student)
        f.close()
    except IOError:
        print('Unable to open file')
    except:
        print('An error has occurred')
    return student_list


# Part (c) Implement assign_students() Function
def assign_students(instructor, group, students):
    for student in students:
        student.group = group
        instructor.add_student(student)
    print('{} students assigned to {}'.format(len(students), instructor.get_name()))

# Test program
group = 'PT01'
instructor = Instructor('may@gmail.com', 'May', 'Lim')
students = load_students()
assign_students(instructor, group, students)
