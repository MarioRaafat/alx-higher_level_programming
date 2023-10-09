#!/usr/bin/python3
def islower(c):
    value = ord(c)
    if value in range(97, 123):
        return True
    else:
        return False
