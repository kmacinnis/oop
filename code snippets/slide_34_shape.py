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

