import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of Circle: {circle.area()}")
print(f"Area of Rectangle: {rectangle.area()}")

'''

Polymorphism allows different classes to define the same method in their own way. In this example, both Circle and Rectangle classes override the area() method, but each calculates the area differently. This enables calling the area() method on any object of type Shape without worrying about its specific class. Polymorphism simplifies code by allowing objects of different shapes to be treated uniformly, making the program more flexible and extensible for future shape types.

'''