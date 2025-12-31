# Contributing to PyToolkit

First off, thank you for considering contributing to PyToolkit! It's people like you that make PyToolkit such a great tool.

## How Can I Contribute?

### Adding New Tools

PyToolkit is designed to be modular. To add a new tool:
1. Create a new file in `src/pytoolkit/tools/` (e.g., `my_tool.py`).
2. Implement your logic using `typer`.
3. Expose a `typer.Typer()` instance as `app`.
4. The tool will be automatically discovered and registered as a subcommand.

Example `my_tool.py`:
```python
import typer
app = typer.Typer(help="My awesome tool description.")

@app.command()
def do_something():
    print("Doing something!")
```

### Reporting Bugs

- Use the GitHub Issues tracker.
- Provide a clear description and steps to reproduce.

### Pull Requests

- Follow the PEP8 style guide.
- Ensure type hints are used.
- Update `requirements.txt` if you add new dependencies.
- Verify your changes by running `python -m pytoolkit --help` or building the binary.

## 🛠️ Development Setup

1. Clone the repository.
2. Initialize virtual environment: `python3 -m venv env`.
3. Install dependencies: `./env/bin/pip install -r requirements.txt`.
4. Set PYTHONPATH: `export PYTHONPATH=$PYTHONPATH:$(pwd)/src`.

## 📦 Building the Binary

Run the provided build script:
```bash
./scripts/build.sh
```
The binary will be generated in the `dist/` directory.

## ⚖️ License

By contributing, you agree that your contributions will be licensed under its MIT License.
