import sys


def main():
    hello("World")
    bye("World")

def hello(name):
    print("hello, ",sys.argv[1],sep="")

def bye(name):
    print("bye, ",sys.argv[1],sep="")

main()
