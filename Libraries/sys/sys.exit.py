import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
#the above line of code doesnot run if no promt given so no Error as it exit in if block itself
#sys,exit---> prints and exits the block