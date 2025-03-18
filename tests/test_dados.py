import pytest
#from dados import *
import random
from dados import lanzar_dado, jugar_turno, determinar_ganador

# ==============================
# Prueba 1: Lanzar Dado
# ==============================
def test_lanzar_dado():
    """Verifica que lanzar_dado() siempre devuelve un valor entre 1 y 6."""
    for _ in range(100):  # Probamos 100 veces
        resultado = lanzar_dado()
        assert 1 <= resultado <= 6, f"Valor inesperado: {resultado}"

# ==============================
# Prueba 2: Jugar un Turno
# ==============================
def test_jugar_turno(monkeypatch, capsys):
    """Simula un turno y verifica que se imprime correctamente."""
    
    def mock_randint(a, b):
        return 4  # Simulamos que siempre sale 4

    monkeypatch.setattr(random, "randint", mock_randint)

    resultado = jugar_turno("Jugador 1")

    captured = capsys.readouterr()
    
    assert resultado == 4, f"Se esperaba 4, pero se obtuvo {resultado}"
    assert "Turno de Jugador 1" in captured.out
    assert "Jugador 1 lanzó un 4" in captured.out

# ==============================
# Prueba 3: Determinar Ganador - Empate
# ==============================
def test_determinar_ganador_empate(monkeypatch, capsys):
    """Simula una partida donde hay empate."""
    
    def mock_randint(a, b):
        return 3  # Ambos jugadores sacan 3

    monkeypatch.setattr(random, "randint", mock_randint)

    determinar_ganador("Jugador 1", "Jugador 2")

    captured = capsys.readouterr()
    
    assert "¡Empate!" in captured.out

# ==============================
# Prueba 4: Determinar Ganador - Jugador 1 gana
# ==============================
def test_determinar_ganador_jugador1(monkeypatch, capsys):
    """Simula una partida donde gana el Jugador 1."""
    
    valores = [5, 2]  # Jugador 1 saca 5, Jugador 2 saca 2

    def mock_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr(random, "randint", mock_randint)

    determinar_ganador("Jugador 1", "Jugador 2")

    captured = capsys.readouterr()
    
    assert "¡Jugador 1 gana!" in captured.out

# ==============================
# Prueba 5: Determinar Ganador - Jugador 2 gana
# ==============================
def test_determinar_ganador_jugador2(monkeypatch, capsys):
    """Simula una partida donde gana el Jugador 2."""
    
    valores = [2, 6]  # Jugador 1 saca 2, Jugador 2 saca 6

    def mock_randint(a, b):
        return valores.pop(0)

    monkeypatch.setattr(random, "randint", mock_randint)

    determinar_ganador("Jugador 1", "Jugador 2")

    captured = capsys.readouterr()
    
    assert "¡Jugador 2 gana!" in captured.out

