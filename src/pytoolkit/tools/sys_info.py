import typer
import psutil
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="💻 System information and utilities.")
console = Console()

@app.command(name="info")
def sys_info():
    """
    Display basic system information (CPU, Memory, OS).
    """
    table = Table(title="System Information")
    table.add_column("Category", style="cyan")
    table.add_column("Value", style="magenta")

    # CPU
    table.add_row("CPU Usage", f"{psutil.cpu_percent()}%")
    table.add_row("CPU Cores", f"{psutil.cpu_count(logical=True)}")

    # Memory
    mem = psutil.virtual_memory()
    table.add_row("Total Memory", f"{mem.total // (1024**3)} GB")
    table.add_row("Used Memory", f"{mem.percent}%")

    # Disk
    disk = psutil.disk_usage('/')
    table.add_row("Disk Usage", f"{disk.percent}%")

    console.print(table)

@app.command(name="usage")
def usage():
    """
    Show live resource usage.
    """
    console.print("[bold yellow]Live monitoring not implemented yet (Phase 4).[/bold yellow]")
