# from turtle import Turtle, scre
# jummy_the_turtle = Turtle

#painting project, drawing the dot.
import turtle as turtle_module

import random
turtle_module.colormode(255)
jum = turtle_module.Turtle()
color_list = [(202,164,189),(172, 154, 40), (238,240,245), (150,75,49), (52,93,124), (223, 201, 135), (140, 30, 19)]

jum.setheading(225)
jum.forward(300)
jum.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    jum.dot(20, random.choice(color_list))
    jum.forward(50)
    if dot_count % 10 == 0:

        jum.setheading(90)
        jum.forward(50)
        jum.setheading(180)
        jum.forward(500)
        jum.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()