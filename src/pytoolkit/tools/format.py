import typer
import json
from rich.console import Console
from rich.syntax import Syntax

app = typer.Typer(help="🎨 Data formatting and prettification.")
console = Console()

@app.command(name="json")
def format_json(
    data: str = typer.Argument(..., help="JSON string to prettify"),
    indent: int = typer.Option(4, help="Indentation levels")
):
    """
    Prettify a JSON string with syntax highlighting.
    """
    try:
        parsed = json.loads(data)
        formatted = json.dumps(parsed, indent=indent)
        syntax = Syntax(formatted, "json", theme="monokai", line_numbers=True)
        console.print(syntax)
    except json.JSONDecodeError as e:
        console.print(f"[bold red]Error parsing JSON:[/bold red] {e}")
