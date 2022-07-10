from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for one_question in question_data:
    question_t = one_question["text"]
    question_a = one_question["answear"]
    new_question = Question(question_t, question_a)
    question_list.append(new_question)


quiz = QuizBrain(question_list)

while quiz.has_quest() == True:
    quiz.next_quest()
print("Dokončili jste kvíz")
print(f"Vaše celkové skóre je: {quiz.score} / {quiz.quest_number}")



