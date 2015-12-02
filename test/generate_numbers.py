import sys
from random import randint

def main():
    numberstring =''
    m = sys.argv[1:][0]
    for i in range(0, int(m)):
        numberstring+=str(randint(0,1000))+' '
    name = 'numbers.txt'
    try:
        file = open(name, 'w')
        file.write(numberstring)
        file.close()
    except:
        print("Something went wrong")
        sys.exit(0)

if __name__ == '__main__':
    print(main())
