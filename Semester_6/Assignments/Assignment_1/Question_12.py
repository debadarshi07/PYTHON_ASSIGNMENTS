class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return Complex(real_sum, imag_sum)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


complex1 = Complex(3, 4)
complex2 = Complex(1, 2)
result = complex1 + complex2

print(f"Sum of complex numbers: {result}")