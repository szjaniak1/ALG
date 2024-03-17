import sys

from lib import *

def main() -> int:
    print(gauss_division(complex(2, 3), complex(3, 2)))
    return 0

if __name__ == '__main__':
    sys.exit(main())
