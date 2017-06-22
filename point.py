"""
#   NAME        :   Robert James Patterson
#   DATE        :   06/15/17
#   FILENAME    :   points.py
#   SYNOPSIS    :   Work file from the 'Strings ans Representations' module of the 'Beyond
#                   Basics' Python course.
"""


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Dunder-str returns a simple string representation of any
    # object. If __str__ is not defined, then __repr__ sill be
    # used by the 'print()' function.
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    # Dunder-repr returns a more complete unambiguous
    # string representation of any object. As a rule,
    # you should always write a repr() for your classes.
    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, f):
        if f == 'r':
            return 'Screen pixel at y={}, x={}'.format(self.y, self.x)
        else:
            return 'Screen pixel at x={}, y={}'.format(self.x, self.y)
