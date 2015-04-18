

def func1(*args):
    print('args = {}'.format(args))
    print('type(args) = {}'.format(type(args)))

def func2(myvar, *args):
    print('myvar = {}'.format(myvar))
    print('args = {}'.format(args))

def func3(myvar, *args, **kwargs):
    print('myvar = {}'.format(myvar))
    print('args = {}'.format(args))
    print('kwargs = {}'.format(kwargs))
    print('type(kwargs) = {}'.format(type(kwargs)))
