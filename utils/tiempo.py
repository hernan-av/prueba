from datetime import datetime

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