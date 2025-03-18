Se instalo lo siguiente

pip install pytest
pip install pygame
Se activo la instalacion de GitHub Actions al crear el directorio: .github/workflows/pytest.yml


Comando para ejecutar pruebas:
PYTHONPATH=. pytest -v --disable-warnings

Deberia funcionar con: pytest -v --disable-warnings

En el archivo pytest.ini lo configuramos para negar algun archivo que ya no queremos que entre a pruebas unitarias
[pytest]
norecursedirs = tests/excluded_tests
addopts = --ignore=tests/test_bricks.py
