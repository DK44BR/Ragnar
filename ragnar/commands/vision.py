import cv2
from rich.console import Console

console = Console()

def vision():
    console.print("[bold green]Abrindo câmera...[/bold green]")
    console.print("[yellow]Pressione Q para sair.[/yellow]")

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        console.print("[red]Erro: não foi possível abrir a câmera.[/red]")
        return

    while True:
        ok, frame = camera.read()

        if not ok:
            break

        cv2.imshow("Ragnar Vision", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    console.print("[green]Câmera encerrada.[/green]")
