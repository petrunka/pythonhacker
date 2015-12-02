import sys

def main():
    filename = 'file.txt'
    data = open(filename, 'r')
    print(data.read())
    data.close()

if __name__ == '__main__':
    print(main())
