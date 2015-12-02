import sys

def main():
    res = ''
    for i in sys.argv[1:]:
        data = open(i, 'r')
        res+=data.read()
        res+='\n'
    return res

if __name__ == '__main__':
    print(main())
