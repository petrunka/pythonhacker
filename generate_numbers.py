import sys
from random import randit

def main():
    a = []
    for i in range(0, sys.argv[1:]):
        a+=randint(1,1000)
    return a

if __name__ == '__main__':
    print(main())
