import os
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel

console = Console()

def mostrar_bienvenida():
    figlet = Figlet(font="slant")
    print(f"[bold magenta]{figlet.renderText('INVENTARIO')}")
    print("📦 Sistema de Gestión - by Hernán\n")

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

from rich.panel import Panel

def mostrar_panel_mensaje(texto: str, estilo: str = "white"):
    console.print(Panel.fit(f"{texto}", border_style=estilo))

def mostrar_error(texto: str):
    mostrar_panel_mensaje(f"❌ {texto}", estilo="red")

def mostrar_exito(texto: str):
    mostrar_panel_mensaje(f"✅ {texto}", estilo="green")