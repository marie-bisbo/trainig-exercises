class Rectangle:
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (self.height + self.width) * 2
