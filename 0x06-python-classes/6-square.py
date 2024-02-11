#!/usr/bin/python3
class Square:

    def __init__(self, size = 0, positions = (0, 0)):
        self.size = size
        self.positions = positions

    def area(self):
        return self.__size ** 2
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for m in range(self.__positions[1]):
            print()
        for i in range(self.__size):
            print("_" * self.__positions[0], end = "") 
            for j in range(self.__size):
                print("#", end = "")
            print()

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("value must be int")
        else:
            if value < 0:
                raise ValueError("value must be >= 0")
            else:
                self.__size = value
    
    @property
    def positions(self):
        return self.positions
    @positions.setter
    def positions(self, value):
        if type(value) is not tuple or len(value) is not 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
         self.__positions = value
