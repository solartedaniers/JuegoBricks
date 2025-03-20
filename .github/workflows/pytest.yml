name: CI - Ejecución de Pruebas Unitarias con Pytest
run-name: Ejecutar pruebas unitarias con Pytest en Python (🧪)

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: 📥 Clonar el repositorio y obtener el código fuente
        uses: actions/checkout@v3

      - name: 🔧 Configurar entorno de Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: 📦 Instalar dependencias del proyecto
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          pip install pytest-html

      - name: 📂 Asegurar que el directorio tests/ existe
        run: mkdir -p $GITHUB_WORKSPACE/tests/

      - name: 🛠️ Generar archivo de pruebas unitarias si no existe
        run: |
          python $GITHUB_WORKSPACE/generate_tests.py
          echo "📂 Listando contenido del directorio tests/ después de la generación:"
          ls -lah tests/

      - name: 🔍 Verificar ubicación de los archivos generados
        run: find $GITHUB_WORKSPACE/tests -type f  

      - name: 📤 Subir archivos generados al repositorio
        run: |
          git config --global user.name "github-actions"
          git config --global user.email "github-actions@github.com"
          git add tests/
          if git diff --cached --quiet; then
            echo "⚠️ No hay cambios nuevos en tests/, omitiendo commit."
          else
            git commit -m "🔧 Agregar archivos de prueba generados automáticamente"
            git push origin main
          fi

      - name: 🧪 Ejecutar pruebas unitarias con Pytest y generar HTML
        run: |
          set +e  # Permite continuar el script si pytest falla
          PYTHONPATH=. pytest $GITHUB_WORKSPACE/tests/ -v --disable-warnings --html=report.html
          EXIT_CODE=$?
          echo "✅ Pruebas ejecutadas, verificando existencia de report.html"
          ls -lah
          exit $EXIT_CODE  # Devuelve el código de error original de pytest

      - name: 📤 Subir reporte de pruebas en HTML a GitHub Actions
        uses: actions/upload-artifact@v4
        with:
          name: pytest-report-html
          path: report.html

      - name: 🔄 Actualizar Codespaces después del push
        run: |
          git remote set-url origin https://github.com/${{ github.repository }}.git
          git pull origin main --rebase