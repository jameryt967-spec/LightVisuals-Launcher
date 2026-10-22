
name: Build LightVisuals EXE

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest

    steps:
      - name: Download source
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install PyInstaller
        run: python -m pip install pyinstaller

      - name: Build EXE
        run: pyinstaller --onefile --windowed --name LightVisuals launcher.py

      - name: Upload EXE
        uses: actions/upload-artifact@v4
        with:
          name: LightVisuals-Windows
          path: dist/LightVisuals.exe
