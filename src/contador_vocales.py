def contar_vocales(texto):
    """Cuenta cuántas vocales hay en un texto."""
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)
