print("  ")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("Hello! Welcome to Turtle Escaping!")
print("This is a game designed for two players.")
print("You will need to decide the Angles and Distances for the turtle,")
print("to escape from the cage.")
print("Player 1 will input 5 angles for turtle.")
print("Player 2 will input 5 distances for turtle")
print("The range for cage will be randomly chosen from 50-375 pixel.")
print("The circle in orange is the cage, and the darkcyan icon is your turtle.")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("  ")
print("  ")
print("  ")

import turtle
import random
import math
rex = turtle.Turtle()
rex.ht()
rex.color("orange","yellow")

t = []
p = []

print("  ")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("For Player1")
print("Please give 5 angles that are diverse from each other and between 0-240.")
for y in range(1,6):
    print(y)
    ranang = input("Please input your angles: ")
    p.append(ranang)
print("  ")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("  ")

print("For Player2")
print("Please give 5 ranges that are diverse from each other and between 0-300.")
for x in range(1,6):
    print(x)
    ranfor = input("Please input your ranges: ")
    t.append(ranfor)
print("  ")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

# r = radius
# p = 2r * pi
# unit forward = p / range = (2r * pi) / range

r = random.randrange(50,376)

rex.ht()
rex.penup()
rex.left(90)
rex.forward(r) # r
rex.right(90)
rex.pendown()
rex.pensize(5)
rex.shapesize(1.2,1.2,3)
rex.st()

rex.begin_fill()
for i in range(90):
    rex.forward((2 * r * math.pi) / 90) # unit forward
    rex.right(4)
rex.end_fill()

rex.ht()
rex.penup()
rex.home()
rex.pendown()
rex.st()

rex.color("darkcyan")
rex.shape("turtle")
rex.pensize(2)
rex.shapesize(1.2,1.2,1)

for i in range(5):
    angle1 = random.choice(p)
    distance1 = random.choice(t)
    rex.right(angle1)
    rex.forward(distance1)
    p.remove(angle1)
    t.remove(distance1)

turtle.done()