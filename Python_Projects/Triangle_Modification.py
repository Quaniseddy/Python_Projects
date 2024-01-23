# Written by Quan Zhang, z5089022 for COMP9021
#
# Defines two classes, Point and Triangle.
#
# An object of class Point is created by passing exactly
# 2 integers as arguments to __init__().
# You can assume that nothing but integers will indeed be
# passed as arguments to __init__(), but not that exactly
# 2 arguments will be provided; when that is not the case,
# a PointError error is raised.
# The point class implements the __str__() and __repr__()
# special methods.
#
# An object of class Triangle is created by passing exactly
# 3 points as keyword only arguments to __init__().
# You can assume that exactly three points will indeed be
# passed as arguments to __init__().
# The three points should not be collinear for the triangle
# to be created; otherwise a TriangleError error is raised.
# A triangle object can be modified by changing one two or three
# points thanks to the method change_point_or_points(),
# all of whose arguments are keyword only.
# At any stage, the object maintains correct values
# for perimeter and area.

import math


class PointError(Exception):
    pass


class Point:
    def __init__(self, x=None, y=None, *n):
        if x is None or y is None or n != ():
            raise PointError("Need two coordinates, point not created.")
        self.x = x
        self.y = y

    def __repr__(self):
        print(f"Point({self.x}, {self.y})")

    def __str__(self):
        print(f"Point of x-coordinate {self.x} and y-coordinate {self.y}")


class TriangleError(Exception):
    pass


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        tmp_area = abs(
            (
                point_1.x * (point_2.y - point_3.y)
                + point_2.x * (point_3.y - point_1.y)
                + point_3.x * (point_1.y - point_2.y)
            )
            / 2
        )
        if tmp_area == 0:
            raise TriangleError("Incorrect input, triangle not created.")

        self.area = tmp_area
        self.perimeter = (
            math.dist((point_1.x, point_1.y), (point_2.x, point_2.y))
            + math.dist((point_2.x, point_2.y), (point_3.x, point_3.y))
            + math.dist((point_1.x, point_1.y), (point_3.x, point_3.y))
        )

    def change_point_or_points(self, *, point_1=None, point_2=None, point_3=None):
        if point_1:
            self.point_1 = point_1
        if point_2:
            self.point_2 = point_2
        if point_3:
            self.point_3 = point_3

        tmp_area = abs(
            (
                self.point_1.x * (self.point_2.y - self.point_3.y)
                + self.point_2.x * (self.point_3.y - self.point_1.y)
                + self.point_3.x * (self.point_1.y - self.point_2.y)
            )
            / 2
        )

        if tmp_area == 0:
            print("Incorrect input, triangle not modified.")
        else:
            self.area = tmp_area
            self.perimeter = (
                math.dist(
                    (self.point_1.x, self.point_1.y), (self.point_2.x, self.point_2.y)
                )
                + math.dist(
                    (self.point_2.x, self.point_2.y), (self.point_3.x, self.point_3.y)
                )
                + math.dist(
                    (self.point_1.x, self.point_1.y), (self.point_3.x, self.point_3.y)
                )
            )
