from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(600,400)
colors = ['red', 'blue', 'green', 'yellow' , 'orange' , 'purple' , 'gray' , 'black' ]
mobility = {}
turtles =[]
bet = ""
winner = ""
x = -200
y = 100
finished = False

def create(turtle1):
    t = Turtle()
    t.penup()
    t.shape("turtle")
    t.color(turtle1)
    t.goto(x,y)
    turtles.append(t)

while bet not in colors :
    bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()

for color in colors :
    create(color)
    y -= 30

while not finished :
    for turtle in turtles :
        if turtle.xcor() >= 200 :
            winner = turtle.pencolor()
            finished = True
            if winner == bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        mobility = random.randint(0,10)
        turtle.forward(mobility)

screen.exitonclick()
