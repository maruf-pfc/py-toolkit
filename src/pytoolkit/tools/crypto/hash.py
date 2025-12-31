import typer
import hashlib
from typing import Optional
from rich.console import Console

app = typer.Typer(help="🔐 Cryptographic utilities and hashing.")
console = Console()

@app.command(name="sum")
def hash_string(
    text: str = typer.Argument(..., help="String to hash"),
    algo: str = typer.Option("sha256", help="Hashing algorithm (md5, sha1, sha256)")
):
    """
    Generate a hash for a given string.
    """
    algo = algo.lower()
    if algo not in hashlib.algorithms_available:
        console.print(f"[bold red]Algorithm {algo} not supported.[/bold red]")
        raise typer.Exit(1)
        
    h = hashlib.new(algo)
    h.update(text.encode())
    console.print(f"[bold green]{algo.upper()}:[/bold green] {h.hexdigest()}")

@app.command(name="file")
def hash_file(
    path: str = typer.Argument(..., help="Path to the file"),
    algo: str = typer.Option("sha256", help="Hashing algorithm")
):
    """
    Generate a hash for a file.
    """
    algo = algo.lower()
    try:
        h = hashlib.new(algo)
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        console.print(f"[bold green]{algo.upper()} ({path}):[/bold green] {h.hexdigest()}")
    except FileNotFoundError:
        console.print(f"[bold red]File not found:[/bold red] {path}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
