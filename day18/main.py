###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import colorgram
from turtle import Turtle,Screen


bebo = Turtle()
rgb_colors = []
color = ()
screen = Screen()
screen.colormode(255)
x = -225
y = -225

x_temp = x
y_temp = y

colors = colorgram.extract('image.jpg', 30)
bebo.up()

for color in colors:
    rgb_colors.append(color.rgb)

screen.title('DAMIEN HIRST')
for n in range(0,10) :
    for i in range(0,10):
         color = random.choice(rgb_colors)
         bebo.goto(x_temp, y_temp)
         bebo.dot(20, (color.r , color.g , color.b))
         x_temp += 50
    bebo.setheading(135)
    y_temp += 50
    x_temp = x

bebo.hideturtle()
screen.exitonclick()

