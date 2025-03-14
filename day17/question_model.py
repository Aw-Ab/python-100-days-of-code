from data import question_data
import random
right_answers = 0
number =0
asked = [] # A list to remember the asked questions
class Question:
    def __init__(self):  # Atributes of a class
        global asked,number
        question = random.choice(question_data)
        self.text = question['text']
        self.answer = question['answer'].lower()
        if question['text'] in asked and len(asked) = len(question_data - 1): # If this is the question has been asked
           self.__init__()
        elif len(asked) >= len(question_data):
             exit("No more questions.")
        else  :
          number += 1
          asked.append(self.text)
    def ask(self): # A method of a class
         global right_answers, number
         self.choice = input(f"Q{number} : {self.text} (True or False) ?").lower()
         if self.choice == 'end' : # A terminator for the game
             print(f"Your final score is : {right_answers}/{number}")
             exit()
         elif self.choice == self.answer : # if the answer is right
             print("You got it right !")
             right_answers += 1
             print(f"Your current score is : {right_answers}/{number}\n")
         elif self.choice not in ['true' , 'false'] : # if the answer is undifined
             print("Unknown answer , Try again .")
             self.ask()
         else : # else the answer is defiend wrong
             print("That is wrong.")
             print(f"The correct answer was: {self.answer}")
             print(f"Your current score is : {right_answers}/{number}\n")



