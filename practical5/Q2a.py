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

def main():
   students = load_result()
   for s in students:
       print(s.name, s.get_score())

def load_result():
   students = []
   try:
       result_file = open('results.txt', 'r')
       for result in result_file:
           list = result.split(',')
           s = Student(list[0])
           s.math = float(list[1])
           s.chinese = float(list[2])
           s.english = float(list[3])
           s.science = float(list[4])
           students.append(s)
   except IOError:
       return 'File cannot be found'
   else:
    return students

main()
