from src.juego_adivina import verificar_adivinanza

def test_verificar_adivinanza():
    assert verificar_adivinanza(5, 5) == "¡Correcto!"
    assert verificar_adivinanza(5, 3) == "Demasiado bajo"
    assert verificar_adivinanza(5, 8) == "Demasiado alto"