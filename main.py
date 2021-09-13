import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('download.jpeg', 30)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors
          if color.rgb.r + color.rgb.g + color.rgb.b <= 600]


def create_spot(turtle, spot_size, color_palette):
    # turtle.color(random.choice(color_palette))
    # turtle.begin_fill()
    turtle.dot(spot_size,random.choice(color_palette))
    # turtle.end_fill()


def create_row(turtle, spot_number, spot_size, space, color_palette):
    for x in range(spot_number-1):
        turtle.pendown()
        create_spot(turtle, spot_size, color_palette)
        turtle.penup()
        turtle.forward(space)

    create_spot(turtle, spot_size, color_palette)


brush = Turtle()
canvas = Screen()
brush.speed('fastest')
canvas.colormode(255)
# canvas.screensize(1280, 1200)

# posiciona turtle no começo da tela
brush.setheading(225)
brush.penup()
brush.forward(300)
brush.setheading(0)
start = brush.position()
brush.hideturtle()

# cria a pintura de acordo com o valor desejado
linhas = 10
colunas = 10

for h in range(1, linhas):
    create_row(brush, colunas, 20, 50, colors)
    brush.goto(start[0], start[1] + (50 * h))

create_row(brush, 10, 20, 50, colors)

canvas.exitonclick()
