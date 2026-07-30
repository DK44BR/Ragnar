from rich.console import Console
import time

console = Console()

def run():
    console.print("[bold cyan]Inicializando Ragnar...[/bold cyan]\n")

    modules = [
        "Brain",
        "Memory",
        "Security",
        "Plugins"
    ]

    for module in modules:
        time.sleep(0.5)
        console.print(f"[green]✓[/green] {module}")

    console.print("\n[bold green]Ragnar ONLINE[/bold green]")
