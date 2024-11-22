class ComplexNumber:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    def __add__(self, other):
        new_real = self._real + other._real
        new_imag = self._imag + other._imag
        return ComplexNumber(new_real, new_imag)
   
    def __sub__(self, other):
        new_real = self._real - other._real
        new_imag = self._imag - other._real
        return ComplexNumber(new_real, new_imag)

    def __str__(self):
        return(f"{self._real} + {self._imag}i")

