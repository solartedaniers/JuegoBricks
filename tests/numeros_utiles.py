# tests/test_numeros_utiles.py

from src.numeros_utiles import es_par, es_primo

def test_es_par():
    assert es_par(2) == True
    assert es_par(3) == False
    assert es_par(0) == True

def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(4) == False
    assert es_primo(1) == False
