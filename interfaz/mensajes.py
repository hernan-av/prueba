import os
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel

console = Console()

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.rule import Rule

console = Console()

def mostrar_bienvenida():
    console.clear()

    titulo = Text("Sistema de Gestión de Inventario", style="bold cyan")
    subtitulo = Text("Trabajo final - Programación 1", style="dim")

    contenido = Align.center(
        f"{titulo}\n{subtitulo}",
        vertical="middle"
    )

    panel = Panel(
        contenido,
        title="[bold green]Bienvenido[/bold green]",
        border_style="green",
        padding=(2, 10),
        style="on grey11",
        expand=True
    )

    console.print(panel)
    console.print(Rule(style="grey50"))


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_panel_mensaje(texto: str, estilo: str = "white"):
    console.print(Panel.fit(f"{texto}", border_style=estilo))

def mostrar_error(texto: str):
    mostrar_panel_mensaje(f"❌ {texto}", estilo="red")

def mostrar_exito(texto: str):
    mostrar_panel_mensaje(f"✅ {texto}", estilo="green")

def mostrar_cancelado(seccion: str):
    mostrar_error(f"Acción cancelada. Volviendo al menú de {seccion}.")
