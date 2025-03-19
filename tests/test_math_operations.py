# tests/test_math_operations.py
import pytest
from src.math_operations import add, subtract, multiply, divide

# ==============================
# Prueba 1: Suma
# ==============================
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# ==============================
# Prueba 2: Resta
# ==============================
def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 7) == -7
    assert subtract(10, 10) == 0

# ==============================
# Prueba 3: Multiplicación
# ==============================
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

# ==============================
# Prueba 4: División
# ==============================
def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):  # Verifica si lanza error con división por cero
        divide(5, 0)
