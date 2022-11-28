from math import pi


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = a

    def area(self):
        return self.a * self.b

    def get_height(self):
        return self.a

    def get_width(self):
        return self.b


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * (self.r) ** 2


main_rect = Rectangle(5, 4)
print(main_rect.area())
main_circle = Circle(2)
print(main_circle.area())
