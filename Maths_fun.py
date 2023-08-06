from turtle import *
speed(0)
def squareShape(length):
    color('blue')
    for counter in range(4):
        forward(length)
        right(90)
        right(2)
    for x in range(180):
        squareShape(120)
    exitonclick()