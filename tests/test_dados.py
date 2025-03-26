import pytest
import builtins
import random
from src.dados import lanzar_dado, jugar_turno, determinar_ganador

def test_lanzar_dado(monkeypatch):
    """Verifica que lanzar_dado siempre devuelva un número entre 1 y 6."""
    for _ in range(10):
        resultado = lanzar_dado()
        assert 1 <= resultado <= 6

def test_jugar_turno(monkeypatch):
    """Verifica que jugar_turno imprima el resultado esperado."""
    mensajes = []
    monkeypatch.setattr(builtins, "print", lambda msg: mensajes.append(msg))
    
    # Simulamos que el dado siempre devuelve 4
    monkeypatch.setattr(random, "randint", lambda a, b: 4)

    resultado = jugar_turno("Jugador 1")
    
    assert mensajes == ["Turno de Jugador 1", "Jugador 1 lanzó un 4"]
    assert resultado == 4

def test_determinar_ganador(monkeypatch):
    """Verifica que determinar_ganador funcione correctamente con valores fijos."""
    mensajes = []
    monkeypatch.setattr(builtins, "print", lambda msg: mensajes.append(msg))
    
    # Simulamos que el primer jugador saca 6 y el segundo 3
    valores_dados = iter([6, 3])
    monkeypatch.setattr(random, "randint", lambda a, b: next(valores_dados))

    determinar_ganador("Jugador 1", "Jugador 2")
    
    assert mensajes[-1] == "¡Jugador 1 gana!"
