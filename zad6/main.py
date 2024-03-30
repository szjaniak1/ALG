import sys

from typing import List
from random import randrange

class set():
    def __init__(self, expo: int, value_func, border_func) -> None:
        self.expo = expo
        self.border_func = border_func
        self.value_func = value_func
        
    def gen_points(self, size: int, low_border: int, high_border: int) -> List:
        res = []
        if size > (high_border - low_border)**2:
            return res
        res_size = 0
        while res_size < size:
            p = []
            for _ in range(self.expo):
                p.append(randrange(low_border, high_border))
            if p not in res and self.border_func(self.value_func(p)):
                res.append(p)
                res_size += 1

        return res

def evaluate(point1: List[int], point2: List[int]) -> bool:
    for (x, y) in zip(point1, point2):
        if x > y:
            return False
    return True

def find_minimal(points: List[List[int]]) -> List[List[int]]:
    minimal = []
    flag = False
    for a in points:
        flag = True
        print(minimal)
        for m in minimal:
            if evaluate(m, a):
                points.remove(a)
                flag = False
                break
            if evaluate(a, m):
                minimal.remove(m)
        if flag:
            minimal.append(a)
            points.remove(a)
        
    return minimal

def func1(point: List[int]) -> int:
    return point[0] * point[1]

def func2(point: List[int]) -> int:
    return ((point[0] - 10)**2 + (point[1] - 10)**2)

def border(value: int) -> bool:
    return value >= 11

def border2(value: int) -> bool:
    return value <= 25

def main() -> int:
    s = set(2, func1, border)
    points = s.gen_points(40, 0, 11)
    minimal = find_minimal(points)
    print(minimal)

    return 0

if __name__ == '__main__':
    sys.exit(main())
