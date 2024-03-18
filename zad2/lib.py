from copy import deepcopy
from typing import List

class polynomial():
    def __init__(self, coeffs: List[int]) -> None:
        self._coeffs = coeffs

    @property
    def coeffs(self) -> List[int]:
        return self._coeffs

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
