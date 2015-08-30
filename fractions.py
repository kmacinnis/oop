
def gcd(a, b):
    """Calculates the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


class Fraction:
    """
    Rational Numbers with support for arthmetic operations.
    Fractions are always reduced when possible.

    >>> a = Fraction(2,3)
    >>> b = Fraction(1,2)
    >>> a + b
    Fraction(7,6)
    >>> a - b
    Fraction(1,6)
    >>> a * b
    Fraction(1,3)
    >>> a/b
    Fraction(4,3)
    """
    def __init__(self, numerator, denominator=1):
        if not all([isinstance(i,int) for i in (numerator,denominator)]):
            raise ValueError('Arguments of Fraction must be integers')
        g = gcd(numerator,denominator)
        self.n = int(numerator/g)
        self.d = int(denominator/g)

    def __neg__(self):
        return Fraction(-self.n,self.d)

    def __abs__(self):
        return Fraction(abs(self.n),abs(self.d))

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return Fraction(n, d)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return Fraction(n1*n2, d1*d2)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return Fraction(n1*d2, d1*n2)

    def __eq__(self, other):
        return (self.n, self.d) == (other.n, other.d)        

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    def __repr__(self):
        return 'Fraction(%s,%s)' % (self.n, self.d)



