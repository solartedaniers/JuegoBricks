# math_operations.py
def add(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

def subtract(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b

def multiply(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b

def divide(a, b):
    """Divide dos números y devuelve el resultado. Lanza un error si b es 0."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
