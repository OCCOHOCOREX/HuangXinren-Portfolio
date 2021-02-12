import turtle
t = turtle.Turtle()

koch = {
    "F": lambda amt: t.forward(amt)
    "+": lambda: t.left(90),
    "-": lambda: t.right(90)
}
def draw(l_string, rule_set):
    if rule_set == "koch":
        rule_set = koch
        t.penup()
        t.setx(-t.screen.screensize()[0]/2)
        t.pendown()
    else:
        raise Exception("Rule set {} is not defined".format(rule_set))

    for state in l_string:
        if state == "F":
            rule_set[state](1000/l_string.count("F"))
        else:
            rule_set[state]()

    turtle.done()

sides = x
def draw_polygon(side_length, x):
    for i in range(0, x):
        t.forward(side_length)
        t.left(360/x)

    turtle.done()

draw_polygon(100, 5)

# x = sides
# internal angle = ((x-2)*180)/x
# external angle = 360/x