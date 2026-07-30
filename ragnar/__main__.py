import typer
from rich.console import Console

from ragnar.commands.doctor import doctor
from ragnar.commands.run import run
from ragnar.commands.flash import flash
from ragnar.commands.vision import vision
from ragnar.commands.hearth import run as hearth

app = typer.Typer(
    help="Ragnar AI - Sistema Operacional de IA Modular"
)

app.command()(doctor)
app.command()(run)
app.command()(flash)
app.command()(vision)
app.command(name="hearth")(hearth)


def main():
    app()


if __name__ == "__main__":
    main()
