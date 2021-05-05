import requests
import html


class Question:
    def __init__(self,question,correct_answer,incorrect_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
    
    def answer_choices(self):
        choices = self.incorrect_answers
        choices.append(self.correct_answer)
        choices.sort()
        return choices

    def is_correct(self, choice):
        return self.correct_answer == choice


def generate_questions():
    URL = "https://opentdb.com/api.php"
    ARGS = {
        'amount' : '10',
        'difficulty' : 'easy',
        'type' : 'multiple',
    }
    response = requests.get(url=URL, params=ARGS)
    data = response.json()
    
    questions = []
    for i in data['results']:
        question = html.unescape(i['question'])
        correct_answer = html.unescape(i['correct_answer'])
        incorrect_answers = [html.unescape(s) for s in i['incorrect_answers'] ]

        q = Question(question, correct_answer, incorrect_answers)
        questions.append(q)
        
    return questions



