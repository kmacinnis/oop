class Triangle(Shape):

    def __init__(self, *args):
        a, b, c = sorted(args)
        if a + b <= c:
            raise ValueError('Cannot construct triangle with sides given.')
        self.sides = (a,b,c)
        super().__init__(*args)

    def area(self):
        semi = sum(self.sides)/2
        a,b,c = self.sides
        return math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))

