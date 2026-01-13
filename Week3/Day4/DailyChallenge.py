# Instructions:

# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.

# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = int(value / 2)

    def circle_area(self):
        return math.pi * self.radius**2
    
    def __str__(self):
        return (f"Circle {self.radius}")
    
    def __add__(self, other):
        if isinstance(other, Circle):
            self.radius + other.radius
            return Circle(self.radius + other.radius)
        else:
            raise TypeError
        
    def __gt__(self, other):
        if isinstance(other, Circle):
            self.radius > other.radius
            return self.radius > other.radius
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Circle):
            self.radius == other.radius
            return self.radius == other.radius
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, Circle):
            self.radius < other.radius
            return self.radius < other.radius
        else:
            return False
        
c1 = Circle(3)
c2 = Circle(7)
c3 = Circle(5)

circles = [c1, c2, c3]
circles.sort()

for c in circles:
    print(c)
