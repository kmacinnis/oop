class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __repr__(self):
        return 'Rectangle(%s,%s)' % (self.width, self.length)

    def area(self):
        return self.width * self.length

    @property
    def diagonal(self):
        return round(sqrt(self.length**2 + self.width**2), 2)