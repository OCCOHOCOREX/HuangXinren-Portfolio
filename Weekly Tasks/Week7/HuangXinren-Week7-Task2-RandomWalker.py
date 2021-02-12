import turtle
import random
wn = turtle.Screen()
wn.bgcolor("darkcyan")
a = turtle.Turtle()
a.color('cyan')

for i in range(10):
    a.forward(random.randrange(0, 101))
    a.right(random.randrange(0,361))

wn.exitonclick()