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


En el paso a paso se genero el archivo requeriments.txt, pero ahora estoy corriendo este comando para ajustar algunos detalles
pip install -r requirements.txt

Datos para ajustar el archivo requirements.txt
(venv) @guswill24 ➜ /workspaces/JuegoBricks (main) $ pytest --version
pytest 8.3.5
El archivo debe quedar asi de acuero a lo que requiere nuestro software:
pygame==2.5.0
pytest==8.3.5
