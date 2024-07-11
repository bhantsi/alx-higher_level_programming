#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    total = sum(int(arg) for arg in argv)
    print(total)
