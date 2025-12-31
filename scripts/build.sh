#!/bin/bash

# Configuration
PROJECT_NAME="pytoolkit"
SRC_DIR="src"
OUTPUT_DIR="dist"
VENV_BIN="./env/bin"

# Ensure venv and pyinstaller are available
if [ ! -d "env" ]; then
    echo "❌ Virtual environment not found. Please run: python3 -m venv env && ./env/bin/pip install -r requirements.txt"
    exit 1
fi

echo "🚀 Starting build for $PROJECT_NAME..."

# Clean previous builds
rm -rf build dist $PROJECT_NAME.spec

# Run PyInstaller
$VENV_BIN/pyinstaller --onefile \
    --name $PROJECT_NAME \
    --paths $SRC_DIR \
    --collect-all pytoolkit \
    --hidden-import typer \
    --hidden-import rich \
    --hidden-import shellingham \
    --hidden-import pytoolkit.core.registry \
    --hidden-import pytoolkit.core.version \
    --hidden-import pytoolkit.tools.sys_info \
    --hidden-import pytoolkit.tools.network \
    --hidden-import pytoolkit.tools.format \
    --hidden-import pytoolkit.tools.crypto \
    --workpath build \
    --distpath dist \
    src/pytoolkit/__main__.py

if [ $? -eq 0 ]; then
    echo "✅ Build successful! Binary located at: dist/$PROJECT_NAME"
    echo "📦 Size: $(du -h dist/$PROJECT_NAME | cut -f1)"
else
    echo "❌ Build failed."
    exit 1
fi
