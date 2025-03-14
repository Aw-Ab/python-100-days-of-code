from turtle import Turtle, Screen

bemo = Turtle()
screen = Screen()

def forwarding():
    bemo.forward(10)

def backing():
    bemo.back(10)

def turning_l():
    new = bemo.heading() + 10
    bemo.setheading(new)

def turning_r():
    new = bemo.heading() - 10
    bemo.setheading(new)


def clearing():
    bemo.clear()
    bemo.penup()
    bemo.home()
    bemo.pendown()



bemo.speed("slowest")
screen.title("| Listening |")

screen.listen()
screen.onkey(forwarding , "w" )
screen.onkey(backing , "s" )
screen.onkey(turning_l , "a")
screen.onkey(turning_r , "d" )
screen.onkey(clearing , "c" )


screen.exitonclick()