import os
import random

def writefile(fileName, inStr):
    with open(fileName, 'w') as f:
        f.write(inStr)


def readfile(fileName):
    with open(fileName, 'r') as f:
        print(f.read())


if __name__ == '__main__':
    name = "output.txt"
    writefile(name, '''hello world!''')
    readfile(name)


    
