import random

class Question:
    def __init__(self, question, option):
        self.question = question
        self.answer = option

class Quiz:
    questions = []
    def __init__(self):
        self.create_question()

    # this method creates 5 random questions and stored in questions class attribute
    def create_question(self):
        q = Question('A bird can fly', 'Y')
        self.__class__.questions.append(q)
        q1 = Question('A dog can fly', 'N')
        self.__class__.questions.append(q1)
        q2 = Question('A cow can fly', 'N')
        self.__class__.questions.append(q2)
        q3 = Question('A bee can fly', 'Y')
        self.__class__.questions.append(q3)
        q4 = Question('A fish can swim', 'Y')
        self.__class__.questions.append(q4)

quiz = Quiz()
score = 0

for i in range(3):
    num = random.randint(0,4-i)
    q = Quiz.questions.pop(num)
    answer = input(q.question + '(Y or N): ')
    if answer.upper() == q.answer :
        score += 1
        print('Yes, you got it right, your score is', score)
    else:
        print('Sorry, you got it wrong, your score is', score)