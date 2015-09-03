class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        super().__init__(width, length)


# class Rectangle(Shape):
#     def __init__(self, *args):
#         self.width, self.length = sorted(args)
#         super().__init__(*args)


