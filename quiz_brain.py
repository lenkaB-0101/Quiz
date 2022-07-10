class QuizBrain:

    def __init__ (self, q_list):
      self.quest_number = 0
      self.score = 0
      self.quest_list = q_list

    def next_quest(self):
        current_quest = self.quest_list[self.quest_number]
        self.quest_number +=1
        user_answer = input(f"Otázka č. {self.quest_number}: {current_quest.text} (T/F): ")
        self.check_answer(user_answer, current_quest.answer)

    def check_answer(self, user_answer, correct_answer):
       if user_answer.lower() == correct_answer.lower():
          print ("Uhádli jste!")
          self.score +=1
       else:
          print("Špatná odpověď")
       print(f"Správná odpověď je: {correct_answer} ")
       print(f"Vaše skóre je: {self.score} / {self.quest_number}")






    def has_quest(self):
      if self.quest_number < len(self.quest_list):
         return True
      else:
         return False


