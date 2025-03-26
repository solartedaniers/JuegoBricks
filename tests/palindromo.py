def es_palindromo(texto):
    """Verifica si un texto es un palíndromo (ignora mayúsculas y espacios)."""
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

