import sys

from lib import *

def main() -> int:
    x = complex_gauss(6, 4)
    y = complex_gauss(3, 2)
    
    q, r = x / y
    print(q, r)
    return 0

if __name__ == '__main__':
    sys.exit(main())
