import os

# Carpeta donde estarán los archivos fuente
SOURCE_DIR = "src"
# Carpeta donde se guardarán las pruebas
TEST_DIR = "tests"

# Código base de prueba para cada archivo detectado
TEST_TEMPLATE = """import pytest
from src.{module} import *  # Importa el módulo desde el paquete src

def test_placeholder():
    assert True  # TODO: Reemplazar con pruebas reales
"""

def generate_test_file(module_name):
    """Genera un archivo de prueba unitaria para un módulo dado dentro de src/."""
    test_file = os.path.join(TEST_DIR, f"test_{module_name}.py")
    
    # Si el archivo de prueba ya existe, no hacer nada
    if os.path.exists(test_file):
        print(f"✔ {test_file} ya existe. No se generó nuevamente.")
        return

    # Crear el código base del test
    test_code = TEST_TEMPLATE.format(module=module_name)

    # Guardar el archivo de prueba
    with open(test_file, "w") as f:
        f.write(test_code)
    
    print(f"✅ Generado: {test_file}")

def main():
    """Detecta nuevos archivos en src/ y genera pruebas automáticamente en tests/."""
    # Crear la carpeta de pruebas si no existe
    os.makedirs(TEST_DIR, exist_ok=True)

    # Buscar archivos Python dentro de src/ (excepto '__init__.py')
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".py") and filename not in ["__init__.py"]:
            module_name = filename[:-3]  # Eliminar la extensión ".py"
            generate_test_file(module_name)

if __name__ == "__main__":
    main()
