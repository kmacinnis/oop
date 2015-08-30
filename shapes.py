import math
import random

COLORS = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']


class GeometryError(ValueError):
    pass


class Shape:
    '''The base class for all our shapes.

    This class doesn't represent any particular shape, it just
    provides the implementation of some methods common to all subclasses.
    '''
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        shape = self.__class__.__name__
        all_args = []
        for arg in self.args:
            all_args.append(repr(arg))
        for kw, arg in self.kwargs.items():
            all_args.append('{0}={1}'.format(kw, repr(arg)))
        comma_sep_args = ', '.join(all_args)
        return '{0}({1})'.format(shape, comma_sep_args)

    def area(self):
        raise NotImplementedError

    @property
    def shape(self):
        return self.__class__.__name__

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.args == other.args) and (self.kwargs == self.kwargs):
            return True
        return False
    



class Rectangle(Shape):

    def __init__(self, width, length, **kwargs):
        self.width, self.length = sorted((width, length))
        super.__init__(self, self.width, self.length, **kwargs)

    def area(self, dp=2):
        return round(self.width*self.length, dp)


class Square(Rectangle):

    def __init__(self, side, **kwargs):
        self.side = side
        super().__init__(self, side, side, **kwargs)
        


class Triangle(Shape):

    def __init__(self, *args, **kwargs):
        a, b, c = sorted(args)
        if a + b <= c:
            raise GeometryError('Cannot construct triangle with sides given.')
        self.sides = (a,b,c)
        super().__init__(*args, **kwargs)

    def area(self):
        semi = sum(self.sides)/2
        a,b,c = self.sides
        return math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))



class Circle(Shape):

    def __init__(self, radius, **kwargs):
        self.radius = radius
        super().__init__(radius, **kwargs)

    def area(self, dp=2):
        return round(math.pi * self.radius**2, dp)


class ColorMixin:
    '''Mixins are a special kind of class,'''
    
    is_colored = True
    
    def __init__(self, *args, **kwargs):
        color = kwargs.pop('color', None)
        if color is None:
            color = random.choice(COLORS)
        super.__init__(*args, **kwargs)


