from copy import deepcopy
from math import ceil, floor

class complex_gauss():
    def __init__(self, a: int, b: int) -> None:
        self._real = a
        self._imag = b

    @property
    def real(self) -> int:
        return self._real
    
    @property
    def imag(self) -> int:
        return self._imag

    def norm(self) -> int:
        return self._real**2 + self._imag**2

    def __add__(self, other) -> 'complex_gauss':
        return complex_gauss(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other) -> 'complex_gauss':
        return complex_gauss(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other) -> 'complex_gauss':
        return complex_gauss(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)

    def __truediv__(self, other) -> tuple['complex_gauss', 'complex_gauss']:
        a1 = (self.real*other.real + self.imag*other.imag) / (other.real**2 + other.imag**2)
        b1 = (self.imag*other.real - self.real*other.imag) / (other.real**2 + other.imag**2)

        a1 = self._round(a1)
        b1 = self._round(b1) 

        q = complex_gauss(a1, b1)
        r = self - (q * other)

        assert r.norm() < other.norm()
        return q, r

    def _round(self, a: float) -> int:
        if a >= 0:
            if a % 1 > 0.5:
                return ceil(a)
            return  floor(a)
        if abs(a) % 1 > 0.5:
            return floor(a)
        return ceil(a)

    def __str__(self) -> str:
        if self.imag >= 0:
            return '(' + str(self.real) + " + " + str(self.imag) + 'i)'
        return '(' + str(self.real) + " - " + str(abs(self.imag)) + 'i)'

def gcd(u: complex_gauss, v: complex_gauss) -> complex_gauss:
    if u.norm() < v.norm():
        return gcd(v, u)

    u_cp = deepcopy(u)
    v_cp = deepcopy(v)

    while True:
        _, r = u_cp / v_cp
        if r.real == 0 and r.imag == 0:
            return v_cp

        u_cp = v_cp
        v_cp = r
