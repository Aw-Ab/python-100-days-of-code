from turtle import Turtle
import random

DISTANCE = 20

class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.shapesize(1 , 5 )
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(pos)
        self.setheading(90)
        self.showturtle()
        self.where = random.choice(["up" , "down"])





    def moving(self):
        if self.where == "up" :
              self.up()
        elif self.where == "down" :
            self.down()
        if self.ycor() >= 360 :
            self.where = "down"
        elif self.ycor() <= -360 :
            self.where = "up"



    def up(self):
        if self.ycor()  >= 360 :
            pass
        else :
                self.forward(DISTANCE)


    def down(self):
        if self.ycor() <= -360:
           pass
        else:
            self.back(DISTANCE)




