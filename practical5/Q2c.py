class Student:
   def __init__(self, name):
       self.name = name
       self.math = 0
       self.chinese = 0
       self.english = 0
       self.science = 0
       self.choices = []

   def get_score(self):
       return (self.math + self.chinese + self.english + self.science) / 4


   def __str__(self):
       return '{} scores {}, the choices are {}, {}, {}'.format(self.name, self.get_score(), self.choices[0], self.choices[1], self.choices[2])

def main():
   students = load_result()
   students = sorted(students, key=by_score, reverse=True)
   for s in students:
       s.choices.append('SchoolA')
       s.choices.append('SchoolB')
       s.choices.append('SchoolC')

   for s in students:
       print(s)

def by_score(student):
   return student.get_score()

def load_result():
   students = []
   result_file = open('results.txt', 'r')
   for result in result_file:
       list = result.split(',')
       s = Student(list[0])
       s.math = float(list[1])
       s.chinese = float(list[2])
       s.english = float(list[3])
       s.science = float(list[4])
       students.append(s)
   return students

main()
