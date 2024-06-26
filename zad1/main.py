import sys

from lib import *

def main() -> int:
    gc1 = complex_gauss(3, 4)
    gc2 = complex_gauss(1, 3)

    c = gcd(gc1, gc2)
    d = lcm(gc1, gc2)
    print(c)
    print(d)
    return 0

if __name__ == '__main__':
    sys.exit(main())
