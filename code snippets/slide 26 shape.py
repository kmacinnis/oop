class Shape:
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
