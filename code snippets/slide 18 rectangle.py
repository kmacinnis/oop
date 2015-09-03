class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


r = Rectangle(3,5)
r.width
r.length
r.area
r.area()
dir(r)
isinstance(r,Rectangle)
r