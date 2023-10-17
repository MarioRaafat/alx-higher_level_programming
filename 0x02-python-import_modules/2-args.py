#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    i = 1
    if count != 1:
        print("{} arguments.".format(count))
        while i < (count + 1):
            print("{}: {}".format(i, sys.argv[i]))
    elif count == 1:
        print("{} argument:".format(count))
