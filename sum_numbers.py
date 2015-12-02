import sys

def main():
    filename = 'numbers.txt'
    data = open(filename, 'r')
    a = data.read()
    b = a.split(' ')
    s = 0
    for i in b:
        s+=i
    return s

if __name__ == '__main__':
    print(main())
