class Sphere:
    def __init__(self,radius=1,x=0,y=0,z=0):
        self.radius=radius
        self.x=x
        self.y=y
        self.z=z
    def get_volume(self):
        return 4/3*3.14*self.radius**3
    def get_square(self):
        return 4*3.14*self.radius**2
    def get_radius(self):
        return self.radius
    def get_center(self):
        return (self.y,self.x,self.z)
    def set_center(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def set_radius(self,radius):
        self.radius=radius
        return self.radius
    def is_point_inside(self,x,y,z):
        if (x-self.x)**2+(y-self.y)**2+(z-self.z)**2<self.radius**2:
            return True
        else:
            return False
sphere=Sphere()
print(sphere.get_center())
print(sphere.get_radius())
print(sphere.get_volume())
print(sphere.get_square())
print(sphere.is_point_inside(0,0,0))