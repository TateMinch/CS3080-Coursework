import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
    def diagonal(self):
        return math.sqrt(self.length ** 2 + self.width**2)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def circumference(self):
        return 2 * math.pi * self.radius
    def diameter(self):
        return 2 * self.radius

class Square:
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length**2
    def perimeter(self):
        return self.length * 4
    def diagonal(self):
        return math.sqrt(self.length**2 + self.length**2)

def main():
    rectangle = Rectangle(20,10)
    circle = Circle(rectangle.diagonal()/2)
    print(circle.circumference())

if __name__ == '__main__':
    main()
