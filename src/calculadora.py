# calculadora.py

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b