import typer
import socket
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

app = typer.Typer(help="🌐 Network utilities and port scanning.")
console = Console()

@app.command(name="scan")
def scan_port(
    host: str = typer.Argument(..., help="Target host (e.g., localhost, 8.8.8.8)"),
    ports: str = typer.Option("80,443,22,3306", help="Comma-separated list of ports to scan"),
    timeout: float = typer.Option(1.0, help="Timeout in seconds for each port")
):
    """
    Scan specific ports on a host to see if they are open.
    """
    port_list = [int(p.strip()) for p in ports.split(",")]
    
    console.print(f"[bold blue]Scanning {host}...[/bold blue]")
    
    open_ports = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(description="Scanning ports...", total=len(port_list))
        
        for port in port_list:
            progress.update(task, description=f"Checking port {port}...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
            progress.advance(task)

    if open_ports:
        console.print(f"[bold green]Open ports on {host}:[/bold green] {', '.join(map(str, open_ports))}")
    else:
        console.print(f"[bold red]No open ports found on {host} in the specified range.[/bold red]")
