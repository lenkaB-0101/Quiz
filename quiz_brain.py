class QuizBrain:

    def __init__ (self, q_list):
      self.quest_number = 0
      self.quest_list = q_list

    def next_quest(self):
        current_quest = self.quest_list[self.quest_number]
        self.quest_number +=1
        input(f"Otázka č. {self.quest_number}: {current_quest.text} (T/F): ")


    def has_quest(self):
      if self.quest_number < len(self.quest_list):
         return True
      else:
         return False
