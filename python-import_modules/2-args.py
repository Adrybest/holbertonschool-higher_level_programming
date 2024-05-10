#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    cnt = len(sys.argv) - 1
    if cnt == 0:
        print("0 arguments.")
    elif cnt == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(cnt))
        for i in range(1, cnt + 1):
            print("{}: {}".format(i, sys.argv[i]))
