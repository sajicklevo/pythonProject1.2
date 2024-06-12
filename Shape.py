class Shape:
    def __init__(self,area,perimetr,draw):
        self.area=area
        self.perimetr=perimetr
        self.draw=draw
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__(width*height,2*width+2*height,True)
        self.width=width
        self.height=height
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(3.14*radius**2,2*3.14*radius,True)
        self.radius=radius
rectangle=Rectangle(4,4)
print(rectangle.area)
print(rectangle.perimetr)
print(rectangle.draw)
circle=Circle(4)
print(circle.area)
print(circle.perimetr)
print(circle.draw)