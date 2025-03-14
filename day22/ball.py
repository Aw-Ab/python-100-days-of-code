from turtle import Turtle
from random import randint


dots = -420

class Ball():

    def __init__(self):
        self.circle = Turtle("circle")
        self.circle.hideturtle()
        self.circle.penup()
        self.circle.color("white")
        self.circle.speed("normal")
        self.circle.setheading(randint(0 , 360))
        self.circle.showturtle()





    def move(self):
        self.circle.forward(20)

    """def line(self):
        global dots
        while dots < 400 :
            dot = Turtle("square")
            dot.hideturtle()
            dot.penup()
            dot.color("white")
            dot.shapesize(0.6 , 0.2)
            dot.teleport(0 , dots)
            dot.showturtle()
            dots += 30
"""
    def bounce_y(self):
        self.circle.setheading(-(self.circle.heading()))

    def bounce_x(self):
        self.circle.setheading(self.circle.heading()+170)

    def reset(self):
        self.circle.clear()
        self.circle.home()
        self.circle.setheading(randint(0 , 360))