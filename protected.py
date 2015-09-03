from shapes import Shape
import math


class Circle(Shape):

    def __init__(self, radius, **kwargs):
        self.__radius = radius
        super().__init__(radius, **kwargs)

    @property
    def radius(self):
        return self.__radius

    @radius.setter # when you do circle.radius = x, it will call this function
    def radius(self, name):
        raise AttributeError("Don't do that!")

    def area(self, dp=2):
        return round(math.pi * self.__radius**2, dp)