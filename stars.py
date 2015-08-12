colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
triples = [ (3,4,5), (5,12,13), (7,24,25), (8,15,17), (9,40,41), 
                        (11,60,61), (12,35,37), (13,84,85), (16,63,65),
                        (20,21,29), (28,45,53), (28,45,53), (36,77,85) ]


def func0(myvar):
    print('myvar = {}'.format(myvar))
    print('type(myvar) = {}'.format(type(myvar)))

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

