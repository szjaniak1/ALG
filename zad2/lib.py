from copy import deepcopy
from typing import List

class polynomial():
    def __init__(self, coeffs: List[int]) -> None:
        self._coeffs = coeffs

    @property
    def coeffs(self) -> List[int]:
        return self._coeffs

    @property
    def deg(self) -> int:
        return len(self.coeffs)

    def __str__(self) -> str:
        return str(self.coeffs)
    
    def __add__(self, other) -> 'polynomial':
        if len(self.coeffs) < len(other.coeffs):
            return other + self

        coeffs_n = deepcopy(self.coeffs) 
        for i in range(len(other.coeffs)):
           coeffs_n[i] = coeffs_n[i] + other.coeffs[i]

        return polynomial(coeffs_n)

    def __sub__(self, other) -> 'polynomial':
        if len(self.coeffs) < len(other.coeffs):
            return other + self

        coeffs_n = deepcopy(self.coeffs) 
        for i in range(len(other.coeffs)):
           coeffs_n[i] = coeffs_n[i] - other.coeffs[i]

        return polynomial(coeffs_n)

    def __truediv__(self, other) -> tuple['polynomial', 'polynomial']:
        q = [0] * (self.deg - other.deg + 1) 
        r = deepcopy(self.coeffs)

        while len(r) >= other.deg:
            curr_expo = len(r) - other.deg
            lead_coeff = r[-1] / other.coeffs[-1]
            q[curr_expo] = lead_coeff
            for i in range(other.deg):
                r[curr_expo + i] = r[curr_expo + i] - lead_coeff * other.coeffs[i]
            r.pop()

        return polynomial(q), polynomial(r)
