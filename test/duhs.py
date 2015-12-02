import sys
import os

def main():
    size = 0
    directory = sys.argv[1:]
    try:
        for i in os.listdir(os.chdir(directory[0])):
            size+=os.path.getsize(i)
    except FileNotFoundError as error:
        print(error)
    return size

if __name__ == '__main__':
    print(main())
