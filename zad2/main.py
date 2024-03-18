import sys

from lib import *

def main() -> int:
    d = polynomial([6, 4])
    z = polynomial([3, 2])
    print(d + z)
    print(d - z)
    q, r = d / z
    print(q)
    print(r)
    print(gcd(d, z))
    print(lcm(d, z))
    return 0

if __name__ == '__main__':
    sys.exit(main())

