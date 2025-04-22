import math

# Base class for solids
class Solid:
    def __init__(self):
        pass
    
    def surface_area(self):
        raise NotImplementedError("Surface area method not implemented.")
    
    def volume(self):
        raise NotImplementedError("Volume method not implemented.")

# Sphere class inheriting from Solid
class Sphere(Solid):
    def __init__(self, radius):
        self.radius = radius
    
    def surface_area(self):
        return 4 * math.pi * self.radius**2
    
    def volume(self):
        return (4/3) * math.pi * self.radius**3

# Cuboid class inheriting from Solid
class Cuboid(Solid):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
    
    def volume(self):
        return self.length * self.width * self.height


# Accept user input for Sphere
print("For Sphere:")
radius = float(input("Enter the radius of the sphere: "))
sphere = Sphere(radius)
print(f"Surface Area of Sphere: {sphere.surface_area():.2f}")
print(f"Volume of Sphere: {sphere.volume():.2f}")

# Accept user input for Cuboid
print("\nFor Cuboid:")
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
cuboid = Cuboid(length, width, height)
print(f"Surface Area of Cuboid: {cuboid.surface_area():.2f}")
print(f"Volume of Cuboid: {cuboid.volume():.2f}")

