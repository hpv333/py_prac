

class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.go_on = True
        self.current_question =[]
    def next_question(self):
        #choice = input(f"Q.{q_number}: {q_bank[q_number]['text']}. True or False?")
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number} {self.current_question.text} True or False ?")
        #choice = choice.lower()
        return choice
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self,user_answer):
        if user_answer == self.current_question.answer:
            print("Correct Answer \n You got it right")
            self.score += 1
        else:
            print("Wrong Answer")
            #self.go_on = False
        print(f"Current Score = {self.score}/{self.question_number}\n")






