#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    count = len(sys.argv) - 1
    total = 0
    i = 0
    while i < count:
        total += int(sys.argv[i + 1])
        i += 1
    print("{}".format(total))
