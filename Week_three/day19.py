from turtle import Turtle, Screen

jum = Turtle()
screen = Screen()
print("W is for forward, S is for backward, R for right and L for left ")

def move_forwards():
    jum.forward(10)

def move_backwards():
    jum.backward(10)

def turn_left():
    new_heading =tim.heading() + 10
    jum.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    jum.setheading(new_heading)

def clear():
    jum.clear()
    jum.home()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
# screen.onkey(key="space", fun= move_forwards)
screen.exitonclick()