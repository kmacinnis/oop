def threeses(x=0):
    while True:
        yield 3**x
        x += 1

class Fiver:
    def __iter__(self):
        return self

    def __next__(self):
        return '5'