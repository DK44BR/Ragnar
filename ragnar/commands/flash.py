from rich.console import Console
from rich.panel import Panel

console = Console()

def flash():
    console.print(
        Panel.fit(
            "[bold cyan]Olá, família![/bold cyan]\n\n"
            "[yellow]Módulo de gravação do ESP32 ainda está em desenvolvimento.[/yellow]",
            title="⚡ Ragnar Flash",
            border_style="green",
        )
    )
