import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Area method not implemented.")
    
    def perimeter(self):
        raise NotImplementedError("Perimeter method not implemented.")

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):  # Circumference
        return 2 * math.pi * self.radius

# Square class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Equilateral Triangle class
class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side

print("Choose a shape:")
print("1. Circle")
print("2. Square")
print("3. Equilateral Triangle")

choice = input("Enter choice (1-3): ")

if choice == '1':
    r = float(input("Enter radius of the circle: "))
    shape = Circle(r)
elif choice == '2':
    s = float(input("Enter side length of the square: "))
    shape = Square(s)
elif choice == '3':
    t = float(input("Enter side length of the triangle: "))
    shape = EquilateralTriangle(t)
else:
    print("Invalid choice.")
    return

print(f"\nArea: {shape.area()}")
print(f"Perimeter/Circumference: {shape.perimeter()}")
