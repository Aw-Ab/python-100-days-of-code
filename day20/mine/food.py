from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create()
        self.refresh()

    def create(self):
        self.shape("circle")
        self.shapesize(0.5 , 0.5 )
        self.color("red")
        self.penup()

    def refresh(self):
        self.teleport(random.randint(-280 , 280) , random.randint(-280 , 280))
