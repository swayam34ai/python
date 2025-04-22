class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        # Represent the complex number as a string in the form 'a + bi'
        return f"{self.real} + {self.imaginary}i"
    
    # Addition of complex numbers
    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)
    
    # Subtraction of complex numbers
    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)
    
    # Multiplication of complex numbers
    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
    
    # Division of complex numbers
    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)

# Create two complex numbers
c1 = ComplexNumber(4, 3)  # 4 + 3i
c2 = ComplexNumber(2, 1)  # 2 + 1i

# Perform operations
print("Complex Number 1:", c1)
print("Complex Number 2:", c2)

# Addition
add_result = c1 + c2
print("Addition Result:", add_result)

# Subtraction
sub_result = c1 - c2
print("Subtraction Result:", sub_result)

# Multiplication
mul_result = c1 * c2
print("Multiplication Result:", mul_result)

# Division
div_result = c1 / c2
print("Division Result:", div_result)
