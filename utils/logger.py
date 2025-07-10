# utils/logger.py
import logging
import os
from datetime import datetime

# Crear carpeta de logs si no existe
LOG_DIR = "./logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Formato del archivo según fecha
fecha_actual = datetime.now().strftime("%Y-%m-%d")
LOG_PATH = os.path.join(LOG_DIR, f"log_{fecha_actual}.log")

# Configuración básica
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] → %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler()  # Quitar si no querés consola
    ]
)

# Atajos convenientes para registrar
def log_info(mensaje: str):
    logging.info(mensaje)

def log_error(mensaje: str):
    logging.error(mensaje)