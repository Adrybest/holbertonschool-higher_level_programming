#!/usr/bin/python3
"""Defnine a class Student."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of a Student."""
        return self.__dict__
