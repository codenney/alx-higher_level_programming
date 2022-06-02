#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    length = len(argv) - 1
    if length < 1:
        print("{0:d} arguments.".format(length))
    elif length == 1:
        print("{0:d} argument:".format(length))
    else:
        print("{0:d} arguments:".format(length))
    for num in range(1, len(argv)):
        print("{0:d}: {1:s}".format(num, argv[num]))
