from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for que in question_data:
    q_1 = Question(que['text'],que['answer'])
    question_bank.append(q_1)
print(question_bank)
#print(type(question_bank))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    user_answer = quiz.next_question()
    quiz.check_answer(user_answer)
print("End of quiz !")
print(f"Final Score = {quiz.score}/{quiz.question_number}")


#go_ahead = True
# shortcut : multiple cursors - double-click ctrl and up or down arrow
# while go_ahead:
#    choice = input("Quiz game !! U ready? y/n")
#    choice = choice.lower()
#    if choice == "y":
#        go_ahead = True
#        q_1 = Question(question_data[0]['text'], question_data[1]['answer'])
#        print(q_1)
#    else:
#        go_ahead = False

