import sys

from typing import List

class set():
    def __init__(self, expo: int, value_func, border_func) -> None:
        self.expo = expo
        self.border_func = border_func
        self.value_func = value_func

def find_minimal(s: set, points: List[List[int]]) -> List[List[int]]:
    minimal = [[]]
    for a in points:
        print("000")
    return minimal

def evaluate(point1: List[int], point2: List[int]) -> bool:
    return False    

def gen_points(k: int, low_border: int, high_border: int) -> List:
    res = []
    return res

def func1(point: List[int]) -> int:
    return point[0] * point[1]

def func2(point: List[int]) -> int:
    return (point[0] - 10)**2 + (point[1] - 10)**2)

def border(value: int) -> tuple[bool, int]:
    return value >= 11, abs(value - 11)

def border2(value: int) -> tuple[bool, int]:
    return value <= 25, abs(value - 25)

def main() -> int:
    points = gen_points(2, 0, 20)
    s = set(2, func1, border)
    minimal = find_minimal(s, points)
    print(minimal)

    return 0

if __name__ == '__main__':
    sys.exit(main())
