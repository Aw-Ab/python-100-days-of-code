from turtle import Turtle

RIGHT_GOALS = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.right_goals = 0
        self.left_goals = 0

