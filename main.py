class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = a

    def area(self):
        return self.a * self.b


main_rect = Rectangle(5, 4)
print(main_rect.area())
