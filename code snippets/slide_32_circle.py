import math

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius)

    def area(self, dp=2):
        return round(math.pi * self.radius**2, dp)

