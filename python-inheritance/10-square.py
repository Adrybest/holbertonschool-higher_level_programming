#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a class Square"""

    def __init__(self, size):
        """Initialize a new Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
