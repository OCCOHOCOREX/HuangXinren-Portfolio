import turtle
t = turtle.Turtle()

class Polygon:
    sides = 0
    length = 0

    def __int__(self, sides, length):
        self.sides = sides
        self.length = length

    def draw(self):
        internal_angle = self.__internal_angle()

        for _ in range(0, self.sides):
            t.forward(self.length)
            t.right(180 - internal_angle)

        turtle.done()

    def __internal_angle(self):
        return ((self.sides - 2) * 180) / self.sides


