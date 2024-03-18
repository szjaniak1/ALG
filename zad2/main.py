import sys

from lib import *

def main() -> int:
    d = polynomial([1, 2, 3])
    z = polynomial([3, 4])
    print(d + z)
    print(d - z)    
    return 0

if __name__ == '__main__':
    sys.exit(main())

