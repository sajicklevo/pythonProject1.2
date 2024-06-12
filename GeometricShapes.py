class GeometricShapes(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius ** 2
        self.perimeter = 2 * 3.14 * radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = 2 * (width + height)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = 0.5 * base * height
        # Assuming equilateral triangle for simplicity in perimeter calculation
        self.perimeter = 3 * base

circle = Circle(4)
print("Circle Area:", circle.area)
print("Circle Perimeter:", circle.perimeter)

rectangle = Rectangle(4, 4)
print("Rectangle Area:", rectangle.area)
print("Rectangle Perimeter:", rectangle.perimeter)

triangle = Triangle(4, 4)
print("Triangle Area:", triangle.area)
print("Triangle Perimeter:", triangle.perimeter)