from myFunctions import *
screen.bgcolor('black')
bob.speed(0)
bob.begin_fill()
bob.pensize(2)
turtle.tracer(0)
for times in range(1000):
  bob.pencolor('white')
  bob.forward(times*4)
  sides = 10
  angle = 360 / sides
  bob.left(angle)
jump(0,0)
'''
for times in range(2):
  shape(0+times*210,0+times*210)
  shape(450+times*210,0+times*210)
  shape(-450+times*210,0+times*210)
  shape(0+times*210,450+times*210)
  shape(0+times*210,-450+times*210)
  shape(450+times*210,450+times*210)
  shape(-450+times*210,-450*times+210)
  shape(450+times*210,-450+times*210)
  shape(-450+times*210,450+times*210)
for times in range(2):
  shape(0-times*210,0-times*210)
  shape(450-times*210,0-times*210)
  shape(-450-times*210,0-times*210)
  shape(0-times*210,450-times*210)
  shape(0-times*210,-450-times*210)
  shape(450-times*210,450-times*210)
  shape(-450-times*210,-450-times*210)
  shape(450-times*210,-450-times*210)
  shape(-450-times*210,450-times*210)
'''
for times in range(5):
  shape(0+times*300,0)
  bob.setheading(20)
  shape(0+times*300,0)
  bob.setheading(360)
  
  
