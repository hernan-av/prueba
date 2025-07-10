import os
from datetime import datetime
import unicodedata

def obtener_fecha_actual():
    """
    Devuelve la fecha y hora actual en formato ISO 8601 compatible con SQLite.

    El formato utilizado es 'YYYY-MM-DD HH:MM:SS', ideal para guardar en campos 
    de tipo TEXT dentro de SQLite, permitiendo ordenamiento y compatibilidad 
    con funciones nativas como date(), datetime() y strftime().

    Returns:
        str: Cadena de texto con la fecha y hora actual, 
            ejemplo '2025-07-02 22:14:58'.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def normalizar_texto(texto: str) -> str:
    return unicodedata.normalize("NFKD", texto.strip().lower()).encode("ASCII", "ignore").decode("utf-8")

def formatear_nombre(texto: str) -> str:
    return texto.strip().title()

def formatear_email(texto: str) -> str:
    return texto.strip().lower()