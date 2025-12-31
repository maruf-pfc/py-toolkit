# 📦 Installation Guide

PyToolkit can be installed in several ways depending on your needs.

## 🚀 1. Pre-built Binaries (Recommended)

This is the easiest way to use PyToolkit without needing Python installed on your system.

1.  Go to the [Releases](https://github.com/maruf-pfc/py-toolkit/releases) page.
2.  Download the binary for your operating system:
    -   `pytoolkit-linux`
    -   `pytoolkit-macos`
    -   `pytoolkit.exe` (Windows)
3.  Make the binary executable (Linux/macOS):
    ```bash
    chmod +x pytoolkit-linux
    ```
4.  Move it to your path:
    ```bash
    sudo mv pytoolkit-linux /usr/local/bin/pytoolkit
    ```

## 🐍 2. From Source (Developers)

If you want to contribute or use the latest development version:

1.  Clone the repo:
    ```bash
    git clone https://github.com/maruf-pfc/py-toolkit.git
    cd py-toolkit
    ```
2.  Create a virtual environment:
    ```bash
    python3 -m venv env
    source ./env/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

### 🐧 Linux GUI Requirements
If you are on Linux and want to use GUI tools (like `graphics img-resize`), you may need to install `tkinter` on your system:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

## 🛠️ 3. Via pip

```bash
pip install git+https://github.com/maruf-pfc/py-toolkit.git
```
