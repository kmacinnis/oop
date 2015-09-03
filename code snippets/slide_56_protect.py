class Circle(Shape):
    def __init__(self, radius, **kwargs):
        self.__radius = radius
        super().__init__(radius, **kwargs)

    @property
    def radius(self):
        return self.__radius

    @radius.setter # circle.radius = <something>  will call this 
    def radius(self, name):
        raise AttributeError("Don't do that!")

    def area(self, dp=2):
        return round(math.pi * self.__radius**2, dp)


