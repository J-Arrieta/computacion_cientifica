"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

#from Point1 import Point, Rectangle, print_point
#from Point1_soln import distance_between_points

import copy

class Point:
    """Represents a point in 2-D space.
    
    Attributes: x, y
    """

    def __init__(self, x, y):
        self.__x, self.__y = x, y

    def print_point(self):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (self.__x, self.__y))

    @property
    def x(self):
        return self.__

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, valor):
        self.__x = valor

    @y.setter
    def y(self, valor):
        self.__y = valor

    def __sub__(self,p):
        dx = self.__x - p.x
        dy = self.__y - p.y
        dist = math.sqrt(dx**2 + dy**2)
        return dist

class Rectangle:
    """Represents a point in 2-D space.
    
    Attributes: corner (Point), width, height
    """
    def __init__(self, x, y, w, h):
        self.__corner = Point(x, y)
        self.__width = w
        self.__height = h

    @property
    def corner(self):
        return self.__corner

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height            


class Circle:
    """Represents a circle.
    
    Attributes: center, radius
    """

    def __init__(self, x, y, r):
        self.__center = Point(x, y)
        self.__radius = r

    @property
    def center(self):
        return self.__center

    @property
    def radius(self):
        return self.__radius

    @center.setter
    def center(self, x, y):
        self.__center.x = x
        self.__center.y = y

    @radius.setter
    def radius(self, r):
        self.__radius = r

    def print_circle(self):
        """Print a Circle object in human-readable format."""
        print('({:.2f}, {:.2f})'.format(self.__center.x, self.__center.y), 'r=%g' % self.__radius)

    def point_in_circle(self, p):
        if self.__center - p == self.__radius:
            return 0
        elif self.__center - p > self.__radius:
            return 1

        return -1
    
    def rect_in_circle(self, rect):
        """Checks whether the corners of a rect fall in/on a circle.
        rect: Rectangle object
        """
        p = rect.corner
        p.print_point()
        if not self.point_in_circle(p):
            return False

        p.x += rect.width
        p.print_point()
        if not self.point_in_circle(p):
            return False

        p.y -= rect.height
        p.print_point()
        if not self.point_in_circle(p):
            return False

        p.x -= rect.width
        p.print_point()
        if not self.point_in_circle(p):
            return False

        return True

__