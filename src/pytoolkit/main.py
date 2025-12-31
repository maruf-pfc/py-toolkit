import typer
from rich.console import Console
from pytoolkit.core.version import __version__
from pytoolkit.core.registry import register_tools

app = typer.Typer(
    name="pytoolkit",
    help="🛠️ PyToolkit: A terminal-based super-fast toolkit collection.",
    add_completion=False,
)

# Register tools dynamically
register_tools(app, "pytoolkit.tools", "pytoolkit.tools")

console = Console()

def version_callback(value: bool):
    if value:
        console.print(f"[bold blue]PyToolkit[/bold blue] version: [green]{__version__}[/green]")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
):
    """
    PyToolkit collection of useful CLI tools.
    """
    pass

if __name__ == "__main__":
    app()
