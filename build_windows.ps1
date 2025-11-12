# Build script for Windows using PyInstaller
# Run this from the project root: .\build_windows.ps1

# Check python
python --version

# Ensure PyInstaller is installed (uncomment to auto-install)
# pip install pyinstaller

# Clean previous builds
if (Test-Path -Path "dist") { Remove-Item -Recurse -Force dist }
if (Test-Path -Path "build") { Remove-Item -Recurse -Force build }
if (Test-Path -Path "saki-doruma.spec") { Remove-Item -Force saki-doruma.spec }

# Collect data files (example: JSON storage files and UI resources)
$datas = @(
    "data/storage/expenses.json;data/storage",
    "data/storage/reports.json;data/storage",
    "ui/stylesheet.py;ui",
)

# Convert datas into --add-data arguments
$addDataArgs = $datas | ForEach-Object { "--add-data `"$_`"" } -join ' '

# Run PyInstaller with recommended flags for GUI apps
pyinstaller --noconfirm --clean --onedir --windowed --name saki-doruma $addDataArgs main.py

Write-Host "Build finished. Output in ./dist/saki-doruma/"