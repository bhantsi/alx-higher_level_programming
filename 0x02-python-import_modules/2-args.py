#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i]))
