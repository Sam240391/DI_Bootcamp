import math
import turtle

class Circle:
    def __init__(self, radius_or_diameter):
        if radius_or_diameter <= 0:
            raise ValueError("Radius or diameter must be greater than zero")
        if radius_or_diameter < 1:
            self.radius = radius_or_diameter / 2
            self.diameter = radius_or_diameter
        else:
            self.radius = radius_or_diameter
            self.diameter = radius_or_diameter * 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError("Unsupported operand type for +: 'Circle' and {}".format(type(other)))

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Unsupported operand type for <: 'Circle' and {}".format(type(other)))

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise TypeError("Unsupported operand type for ==: 'Circle' and {}".format(type(other)))


c1 = Circle(5)
c2 = Circle(3)

print(c1.radius)  
print(c1.diameter)  
print(c1.area())  

c3 = c1 + c2
print(c3.radius)  
print(c3.diameter) 

print(c1 < c2)  
print(c1 == c2)  


circles = [Circle(4), Circle(2), Circle(6), Circle(1)]
sorted_circles = sorted(circles)
for circle in sorted_circles:
    print(circle)


def draw_circle(circle):
    turtle.circle(circle.radius * 10)

turtle.speed(0)  
for circle in sorted_circles:
    draw_circle(circle)
turtle.done()