from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.teleport(0 ,270)
        self.color("white")
        self.update_board()

    def update_board(self):
        self.write(f"Score : {self.score}", False, "center" , ('Arial' ,22 ,'normal'))

    def increase(self):
        self.clear()
        self.score += 1
        self.update_board()


    def game_over(self):
        self.clear()
        self.home()
        self.color("red")
        self.write(f"Game Over ! \nFinal score : {self.score}" , False , "center" ,('Arial' ,24 ,'bold') )