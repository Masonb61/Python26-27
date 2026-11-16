import turtle
from random import randint
bob = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()


def polygon(color,sides,length):
    angle = 360 / sides
    bob.begin_fill()
    for num in range(sides):
        bob.forward(length)
        bob.left(angle)
    bob.end_fill()
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
def comet(color,angle,length):
    
    for num in range(25):
        bob.width(num*0.7)
        bob.forward(length)
        bob.left(angle)
def shape(x,y):
    jump(x,y)
    for times in range(250):
        co = (0,0,times)
        bob.pencolor(co)
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        c = (0,times,times)
        bob.fillcolor(c)
        comet(c,10000,9)
        bob.forward(times*1.3)
        bob.left(93)
