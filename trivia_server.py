from bottle import get, request, static_file, run, post
from random import randint
import json

questions = {
    "homer": [{"question": "can you make a dog noise?", "ans": "4", "answers": ["tweet", "moo", "miao", "woof"]}],
    "easy": [{"question": "what is the capital of israel?", "ans": "2", "answers": ["Tel aviv", "jerusalem", "Aman", "new york"]}],
    "medium": [{"question": "how long is a fortnight?", "ans": "2", "answers": ["week", "2 weeks", "a month", "a year"]}],
    "hard": [{"question": "What is Obama's height?", "ans": "3", "answers": ["1.73", "2.00", "1.85", "1.60"]}]
}


@get('/add_question')
def question_form():
    return static_file("question.html", root="")


@post('/add_question')
def add_question():
    level = request.forms.get('level')
    new_question = {}
    new_question["question"] = request.forms.get('question')
    new_question["ans"] = request.forms.get('ans')
    new_question["answers"] = []
    new_question["answers"].append(request.forms.get('ans1'))
    new_question["answers"].append(request.forms.get('ans2'))
    new_question["answers"].append(request.forms.get('ans3'))
    new_question["answers"].append(request.forms.get('ans4'))
    questions[level].append(new_question)
    return "SUCCESS: level contains " + str(len(questions[level])) + " questions"


@get('/get_question')
def get_question():
    level = request.query['level']
    index = randint(0, len(questions[level]) - 1)
    return json.dumps(questions[level][index])

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')

@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')

@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


if __name__ == "__main__":
    run(host="localhost", port=7000, debug=True)
