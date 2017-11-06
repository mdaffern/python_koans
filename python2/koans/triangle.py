#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    return_value = 'scalene'
    args = [a, b, c]

    for arg in args:
        if arg <= 0:
            raise TriangleError("All sides should be greater than 0")

    if a + b < c or b + c < a or a + c < b:
        raise TriangleError("The sum of any two sides should be greater than the third one")


    if a == b == c:
        return_value = 'equilateral'
    elif a == b or b == c or a == c:
        return_value = 'isosceles'

    return return_value


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
