Windows build instructions (PyInstaller)

Prerequisites
- Python 3.8+ installed and on PATH
- pip
- PySide6 installed (your `requirements.txt` already lists PySide6==6.7.0)
- PyInstaller (install with `pip install pyinstaller`)

Quick steps
1. Install PyInstaller:

   pip install pyinstaller

2. From the project root run the build script in PowerShell (recommended):

   .\build_windows.ps1

This script will:
- remove previous `dist` and `build` folders
- run PyInstaller with `--onedir` and `--windowed`
- include the `data/storage/*.json` files and `ui/stylesheet.py` as example data

Notes & tips
- Use `--onedir` first because bundling PySide6 into a single-file (`--onefile`) can require extra testing for Qt plugins.
- If the app complains about missing Qt platforms (e.g. "could not find or load the Qt platform plugin windows"), run PyInstaller with hooks or add the PySide6 plugin folder manually. The PyInstaller hook for PySide6 often handles this, but if not, try adding:

   --add-binary "$(python -c \"import PySide6; import os; print(os.path.join(os.path.dirname(PySide6.__file__), 'plugins'))\");PySide6/plugins"

- For larger apps you may need to create a `.spec` file and add `hiddenimports` or `datas` explicitly.

Troubleshooting
- If the executable fails to start, run the one in `dist/saki-doruma/` from PowerShell (not double-click) to see console output (remove `--windowed` to keep console open during troubleshooting).
- Common missing items: fonts, Qt platform plugins, additional dynamic libraries. The build log and runtime console output will indicate missing modules.

Advanced: create a `.spec` if you need fine-grained control. Ask me and I can generate one tailored to this project.