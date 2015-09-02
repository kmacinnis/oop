###### First Example #####

class X:
    pass

class Y(X):
    pass

class W:
    pass

class Z(W):
    pass

class J:
    pass

class Alpha(Y,J,Z):
    pass




##### Second Example #####

class A:
    def foo(self):
        print('foo from A')


class B(A):
    def foo(self):
        print('foo from B')
        super().foo()
    
    def bar(self):
        print('bar from B')


class C(A):
    def foo(self):
        print('foo from C')
        super().foo()

    def bar(self):
        print('bar from C')


class D(B,C):
    def foo(self):
        print('foo from D')
        super().foo()



##### Third Example #####

# class First:
#     pass
#
# class Second(First):
#     pass
#
# class Third(First, Second):
#     pass


