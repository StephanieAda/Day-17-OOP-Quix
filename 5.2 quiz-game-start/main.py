from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    question_add = Question(question_text, question_answer)
    question_bank.append(question_add)


# print(question_bank[0].text)

question = Quiz(question_bank)
# okay = question.question_list['text']
question.next_question()
