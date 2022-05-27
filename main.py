from turtle import Turtle, Screen, colormode
import colorgram
from random import choice

colors = colorgram.extract('images.jpg', 30)

paint = Turtle()
my_screen = Screen()
paint.speed('fastest')
paint.penup()
paint.hideturtle()
colormode(255)

def random_color():
    random_color = choice(colors)
    rgb = random_color.rgb
    return (rgb.r , rgb.g , rgb.b)
    
for y in range(-250, 251, 40):
    for x in range(-350, 351, 40):
        get_color = random_color()
        paint.goto(x, y)
        paint.dot(18, get_color)

my_screen.exitonclick()