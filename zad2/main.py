import sys

from lib import *

def main() -> int:
    p1 = polynomial([1, 0, 1])
    p2 = polynomial([1, 2, 1])

    c_x = gcd(p1, p2)
    d_x = lcm(p1, p2)

    print(c_x)
    print(d_x)
    return 0

if __name__ == '__main__':
    sys.exit(main())

