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

    def set_height(self, a):
        self.a = a

    def set_width(self, b):
        self.b = b

    def perimeter(self):
        return self.a * 2 + self.b * 2


main_rect = Rectangle(5, 4)
print(main_rect.area())
print(main_rect.perimeter())
